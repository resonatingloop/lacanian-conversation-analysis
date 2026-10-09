#!/usr/bin/env python3
"""Validate the public fictional fixture suite without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
SCHEMA = ROOT / "schemas" / "conversation-event.schema.json"

EXPECTED_KEYS = {
    "fixture_status",
    "case_purpose",
    "must_notice",
    "may_infer",
    "live_alternatives",
    "must_not_claim",
    "warranted_concepts",
    "unwarranted_concepts",
}

ALLOWED_MESSAGE_KEYS = {
    "ref",
    "order",
    "speaker",
    "content",
    "timestamp",
    "reply_to",
    "participant_kind",
    "relay",
    "provenance",
    "attachments",
}

ALLOWED_PARTICIPANT_KINDS = {"human", "agent", "relay", "system", "unknown", None}
ALLOWED_ORDERING = {"source-order", "timestamp", "declared-order", "unknown"}
CONCEPTS = {
    "sequence-and-repair",
    "enunciation-and-enunciated",
    "signifier-and-chain",
    "subject-position-and-address",
    "supposed-knowledge",
    "organizing-signifier",
}

PRIVATE_MARKERS = {
    ".private/",
    "do-not-publish",
    "private-lookup.json",
    "private-source/",
    "working-trace/",
}


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: cannot read valid JSON: {exc}") from exc


def validate_schema_document() -> list[str]:
    errors: list[str] = []
    schema = read_json(SCHEMA)
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append("schema must declare JSON Schema draft 2020-12")
    if schema.get("properties", {}).get("profile", {}).get("const") != "conversation-event/v0.1":
        errors.append("schema must pin conversation-event/v0.1")
    if set(schema.get("required", [])) != {"profile", "conversation_ref", "messages"}:
        errors.append("schema root required fields changed unexpectedly")
    return errors


def validate_event(event: Any, label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(event, dict):
        return [f"{label}: event must be an object"]
    if event.get("profile") != "conversation-event/v0.1":
        errors.append(f"{label}: profile must be conversation-event/v0.1")
    if not isinstance(event.get("conversation_ref"), str) or not event["conversation_ref"]:
        errors.append(f"{label}: conversation_ref must be a non-empty string")
    if event.get("ordering_basis") not in ALLOWED_ORDERING:
        errors.append(f"{label}: ordering_basis must be declared")

    messages = event.get("messages")
    if not isinstance(messages, list) or len(messages) < 2:
        return errors + [f"{label}: messages must contain at least two items"]

    refs: set[str] = set()
    orders: list[int] = []
    for index, message in enumerate(messages):
        prefix = f"{label}: messages[{index}]"
        if not isinstance(message, dict):
            errors.append(f"{prefix} must be an object")
            continue
        unknown = set(message) - ALLOWED_MESSAGE_KEYS
        if unknown:
            errors.append(f"{prefix} has unknown fields: {sorted(unknown)}")
        for field in ("ref", "speaker", "content"):
            if not isinstance(message.get(field), str) or (field != "content" and not message[field]):
                errors.append(f"{prefix}.{field} must be a valid string")
        ref = message.get("ref")
        if isinstance(ref, str):
            if ref in refs:
                errors.append(f"{prefix}.ref duplicates {ref}")
            refs.add(ref)
        order = message.get("order")
        if not isinstance(order, int) or isinstance(order, bool) or order < 0:
            errors.append(f"{prefix}.order must be a non-negative integer")
        else:
            orders.append(order)
        if message.get("participant_kind") not in ALLOWED_PARTICIPANT_KINDS:
            errors.append(f"{prefix}.participant_kind is not permitted")

    if orders != sorted(orders) or len(orders) != len(set(orders)):
        errors.append(f"{label}: message order values must be strictly increasing")

    for index, message in enumerate(messages):
        if not isinstance(message, dict):
            continue
        reply_to = message.get("reply_to")
        if reply_to is not None and reply_to not in refs:
            errors.append(f"{label}: messages[{index}].reply_to references missing {reply_to}")

    return errors


def validate_expectations(expectations: Any, label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(expectations, dict):
        return [f"{label}: expectations must be an object"]
    missing = EXPECTED_KEYS - set(expectations)
    unknown = set(expectations) - EXPECTED_KEYS
    if missing:
        errors.append(f"{label}: missing expectation fields: {sorted(missing)}")
    if unknown:
        errors.append(f"{label}: unknown expectation fields: {sorted(unknown)}")
    if expectations.get("fixture_status") != "wholly-fictional":
        errors.append(f"{label}: fixture_status must be wholly-fictional")
    if not isinstance(expectations.get("case_purpose"), str) or not expectations["case_purpose"]:
        errors.append(f"{label}: case_purpose must be a non-empty string")

    for field in EXPECTED_KEYS - {"fixture_status", "case_purpose"}:
        value = expectations.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
            errors.append(f"{label}: {field} must be a list of non-empty strings")
    for field in ("must_notice", "live_alternatives", "must_not_claim"):
        if isinstance(expectations.get(field), list) and not expectations[field]:
            errors.append(f"{label}: {field} must not be empty")

    warranted = set(expectations.get("warranted_concepts", []))
    unwarranted = set(expectations.get("unwarranted_concepts", []))
    unknown_concepts = (warranted | unwarranted) - CONCEPTS
    if unknown_concepts:
        errors.append(f"{label}: unknown concept keys: {sorted(unknown_concepts)}")
    if warranted & unwarranted:
        errors.append(f"{label}: concepts cannot be both warranted and unwarranted")
    return errors


def validate_private_markers(fixture_dir: Path) -> list[str]:
    errors: list[str] = []
    uuid_pattern = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", re.I)
    for path in sorted(fixture_dir.glob("*.json")):
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for marker in PRIVATE_MARKERS:
            if marker in lowered:
                errors.append(f"{path.relative_to(ROOT)} contains forbidden private marker {marker!r}")
        if uuid_pattern.search(text):
            errors.append(f"{path.relative_to(ROOT)} contains a UUID-like identifier")
    return errors


def validate_all() -> tuple[int, list[str]]:
    errors = validate_schema_document()
    fixture_dirs = sorted(path for path in FIXTURES.iterdir() if path.is_dir())
    if len(fixture_dirs) < 6:
        errors.append(f"expected at least six fixtures, found {len(fixture_dirs)}")
    for fixture_dir in fixture_dirs:
        label = fixture_dir.name
        event_path = fixture_dir / "event.json"
        expectations_path = fixture_dir / "expectations.json"
        if not event_path.is_file() or not expectations_path.is_file():
            errors.append(f"{label}: requires event.json and expectations.json")
            continue
        errors.extend(validate_event(read_json(event_path), label))
        errors.extend(validate_expectations(read_json(expectations_path), label))
        errors.extend(validate_private_markers(fixture_dir))
    return len(fixture_dirs), errors


def main() -> int:
    count, errors = validate_all()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"validated {count} wholly fictional fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

