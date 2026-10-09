# Public contracts

This document defines the observable behavior of `lacanian-conversation-analysis` version `0.1`. The terms MUST, MUST NOT, SHOULD, and MAY are normative.

## 1. Input contract

The skill accepts an ordered conversation or a bounded excerpt from one. Human, agent, and mixed-participant conversations are all in scope.

The minimum sufficient input is:

1. an order for each message or conversational unit;
2. a local reference for each unit;
3. a speaker label;
4. content.

Timestamps, reply targets, relay information, participant kinds, platform metadata, provider/model/version data, attachments, and source provenance MAY be supplied. Unknown fields MUST remain unknown. The analyst MUST NOT fabricate missing reply targets, chronology, identity, or provenance.

Plain text and Markdown are valid inputs. `schemas/conversation-event.schema.json` is an optional normalized interchange profile, not a condition of use.

## 2. Source and annotation contract

Observed source facts and analytical annotations MUST remain distinguishable.

- Source facts include supplied wording, order, explicit speaker labels, timestamps, reply edges, and declared provenance.
- Annotations include inferred address, subject position, phase, organizing signifier, relational operation, and causal account.

The analysis MUST use four epistemic statuses:

1. **Direct evidence** — observable in the supplied record.
2. **Strong inference** — best explanation of multiple observations with downstream support.
3. **Plausible alternative** — a live account compatible with the record.
4. **Speculation** — generative but weakly constrained by the record.

A claim MUST identify its evidence references and status. Confidence language MUST NOT replace this status structure.

## 3. Sequential method contract

The analyst MUST:

1. state the supplied boundary and important missing context;
2. read the conversation in order before selecting luminous excerpts;
3. trace explicit and inferred address, reply, relay, and uptake;
4. identify candidate phase changes from changes in interactional function, not topic alone;
5. compare attempted repairs by what changes in subsequent turns;
6. distinguish local generation behavior, recurring participant pattern, and room-produced effect when the evidence allows;
7. perform an adversarial pass against the preferred account;
8. state what is not established.

The analyst MUST NOT treat temporal adjacency by itself as proof of causality.

## 4. Lacanian warrant contract

Lacanian terminology MUST earn its place through an operational question and evidence requirement recorded in `references/lacanian-warrant.md`.

Every Lacanian claim MUST provide:

- the concept used;
- the observable conversational phenomenon it helps distinguish;
- the cited event references;
- the concept-specific limitation or disallowed inference;
- a source from `references/sources.md` when the concept is explained or contested.

The analyst MUST NOT force unused concepts into the analysis. Frequency alone does not establish a master signifier. A subject position is not a personality type. A reading of enunciation is not proof of unconscious intention.

## 5. Output contract

The default profile is `response/v0.1`. The optional long-form profile is `markdown-dossier/v0.1`. Both are defined in `references/output-profiles.md`.

The response profile MUST contain:

- scope and conditions;
- a relational thesis;
- sequence and candidate phase boundaries;
- claims with epistemic status and event references;
- Lacanian concepts used and their warrants;
- alternatives or counterevidence;
- an adversarial limitation;
- what is not established.

The dossier profile MUST use the predefined section order and claim-ledger fields. It is returned inline unless the user explicitly asks for a file and supplies or accepts a destination.

Exact prose is not canonical. Structure, traceability, and prohibited overclaims are canonical.

## 6. Privacy and persistence contract

Supplied conversations are private by default. Running the analysis does not imply permission to publish, upload, quote publicly, train on, or persist them.

The skill itself requires no network call, external account, telemetry, or durable storage. A host MAY provide such capabilities, but the analyst MUST NOT use them for conversation content without explicit user direction.

Direct quotation in an analysis is not publication consent. When the output may become public, the analyst SHOULD prefer opaque local references and non-reconstructive paraphrase unless quotation permission is explicit and case-specific.

## 7. Versioning contract

- `conversation-event/v0.1`, `response/v0.1`, and `markdown-dossier/v0.1` are independently named contracts.
- Backward-compatible clarifications MAY retain the profile version.
- New required fields, changed section semantics, or relaxed privacy guarantees require a new profile version.
- Experimental status MUST remain visible until a non-synthetic, openly publishable comparison case has informed the method.

