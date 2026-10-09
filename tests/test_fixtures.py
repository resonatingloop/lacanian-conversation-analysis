from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_fixtures.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("fixture_validator", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load fixture validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


class FixtureContractTests(unittest.TestCase):
    def test_all_fixtures_satisfy_contract(self) -> None:
        count, errors = VALIDATOR.validate_all()
        self.assertGreaterEqual(count, 6)
        self.assertEqual(errors, [])

    def test_cases_cover_declared_structural_risks(self) -> None:
        purposes = []
        for path in sorted((ROOT / "tests" / "fixtures").glob("*/expectations.json")):
            purposes.append(json.loads(path.read_text(encoding="utf-8"))["case_purpose"])
        joined = " ".join(purposes).lower()
        for term in ("negative control", "position", "relay", "repair", "signifier", "provenance"):
            self.assertIn(term, joined)

    def test_fixtures_define_prohibited_overclaims(self) -> None:
        for path in sorted((ROOT / "tests" / "fixtures").glob("*/expectations.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(path=path.parent.name):
                self.assertTrue(data["must_not_claim"])
                self.assertTrue(data["live_alternatives"])


class PackageContractTests(unittest.TestCase):
    def test_repository_has_exactly_one_skill_manifest(self) -> None:
        manifests = [path for path in ROOT.rglob("SKILL.md") if ".git" not in path.parts]
        self.assertEqual(manifests, [ROOT / "SKILL.md"])

    def test_skill_frontmatter_and_runtime_guarantee(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: lacanian-conversation-analysis\n"))
        self.assertIn("description:", text.split("---", 2)[1])
        self.assertIn("requires no network", text.lower())

    def test_dossier_template_has_required_sections(self) -> None:
        text = (ROOT / "assets" / "markdown-dossier-template.md").read_text(encoding="utf-8")
        required = (
            "Scope, trace, and privacy conditions",
            "Relational thesis",
            "Sequence and candidate phase boundaries",
            "Relational geometry",
            "Organizing signifiers",
            "Rupture, failed repair, and effective repair",
            "Claim ledger",
            "Lacanian warrant",
            "Alternatives and counterevidence",
            "Adversarial pass",
            "Limits and what is not established",
            "Sources",
        )
        for heading in required:
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_worked_examples_declare_profiles_and_fictional_sources(self) -> None:
        examples = sorted((ROOT / "examples").glob("*.md"))
        self.assertEqual(len(examples), 2)
        for path in examples:
            text = path.read_text(encoding="utf-8").lower()
            with self.subTest(path=path.name):
                self.assertIn("profile:", text)
                self.assertIn("wholly fictional fixture", text)
                self.assertIn("not established", text)

    def test_no_third_party_source_text_is_bundled(self) -> None:
        prohibited_suffixes = {".pdf", ".epub", ".doc", ".docx"}
        bundled = [path for path in ROOT.rglob("*") if path.is_file() and path.suffix.lower() in prohibited_suffixes]
        self.assertEqual(bundled, [])


if __name__ == "__main__":
    unittest.main()

