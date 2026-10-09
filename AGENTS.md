# Repository instructions

## Mission

Maintain a portable, evidence-led protocol for Lacanian-style conversation analysis. The event record outranks an elegant interpretation.

## Public-source boundary

- Never add a private transcript, private case excerpt, private identifier, or reconstructive paraphrase.
- Examples and tests must be wholly fictional or come from a source whose license explicitly permits redistribution.
- Public access is not a redistribution license. Link to citation-only sources; do not vendor them.
- Preserve the distinction between observed event data, inference, alternatives, and speculation.

## Method boundary

- Sequence, address, uptake, repair, and downstream effects are load-bearing.
- Lacanian concepts require the warrant described in `references/lacanian-warrant.md`.
- A concept is optional even when it is available. Do not force a complete Lacanian taxonomy onto every case.
- Do not infer persistent interior states, clinical structures, or model-wide dispositions from a local exchange.

## Change protocol

- Update `CONTRACTS.md` when observable behavior changes.
- Update `STATUS.md` after verification.
- Put material implementation decisions in a numbered file under `specs/`; retire the spec after the accepted slice is complete.
- Run `python3 scripts/validate_fixtures.py` and `python3 -m unittest discover -s tests -v` before reporting a material change complete.
- Keep exactly one `SKILL.md`, at the repository root.

## Documentation authority

- `PROJECT_BRIEF.md`: product intent and boundaries.
- `CONTRACTS.md`: normative public behavior.
- `SKILL.md`: runtime routing and procedure.
- `references/`: method detail and scholarship.
- `schemas/`: optional normalized interchange.
- `tests/fixtures/`: synthetic behavioral evidence, not canonical prose.
- `STATUS.md`: current verification and remaining release gates.

