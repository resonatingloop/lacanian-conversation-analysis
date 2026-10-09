# Spec 002: numbered example suite

Status: retired

- Accepted: 2026-10-09
- Retired: 2026-10-09
- Authorization: owner accepted the proposed suite and explicitly cleared implementation
- Scope: four additional end-to-end synthetic conversation/analysis pairs

## Context

Example 001 demonstrates a clear positive case: epistemic provenance shifts, the participant names the operative distinction, and a locally successful repair follows. The public suite also needs to show that the method can refuse a seductive interpretation, preserve genuine indeterminacy, separate quoted from current voice, and distinguish social address continuity from runtime-model discontinuity.

## Change-shape matrix

| Dimension | Changed? | Source of truth | Proof |
|---|---:|---|---|
| User-visible behavior | Yes | `examples/`, `README.md` | Manual review plus bundle-structure test |
| Persisted state or schema | No | `schemas/`, unchanged | Diff inspection |
| External or provider-visible behavior | No | No provider integration | Diff inspection |
| Identifiers, secrets or privacy | Yes | `AGENTS.md` public-source boundary | Fictional-source declarations and clean-room scan |
| Lifecycle or terminal states | No | No runtime lifecycle | Diff inspection |
| Setup, operation or recovery | No | Existing validation commands | Full required suite |
| Normative contract or decision | No | `CONTRACTS.md`, unchanged | Contract comparison |
| Cross-repository dependency | No | Repository-local examples | Tree inspection |

## In scope

1. `examples/002/`: an adversarial case whose mythic reading is undercut by trace evidence.
2. `examples/003/`: an ambiguous case with two live structural branches and one named missing discriminator.
3. `examples/004/`: a quotation/relay case separating current speaker, attributed source, quoted language, recommendation, address, and uptake.
4. `examples/005/`: a model-runtime change under one stable speaker label, separating room-level office continuity from generator continuity.
5. A concise README index for numbered examples.
6. Structural regression proof that numbered case directories are contiguous and keep source separate from analysis.
7. Reconciled current status.

## Out of scope

- New Lacanian concepts or changes to the warrant registry
- Changes to input, output, privacy, or versioning contracts
- Machine scoring of analytical prose
- Publication, commit, or push
- A single omnibus example combining all stressors

## Example invariants

- Each numbered directory contains exactly `conversation.md` and `analysis.md`.
- Conversation files contain only synthetic source material and source metadata, not an answer key or analytical headings.
- Analysis files use `response/v0.1`, preserve the evidence ladder, name live alternatives, run an adversarial pass, and state what is not established.
- The adversarial example is defeated by evidence inside the trace, not by an external preferred interpretation.
- The ambiguous example supports firm local claims while leaving one consequential branch unresolved.
- The relay and runtime-change examples preserve supplied provenance distinctions without inferring identity or interior continuity.

## Validation

```bash
python3 scripts/validate_fixtures.py
python3 -m unittest discover -s tests -v
python3 /home/resonatingloop/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 /home/resonatingloop/.codex/skills/manage-project-docs/scripts/check_docset.py .
git diff --check
```

## Acceptance evidence

- All five numbered directories are contiguous and structurally complete.
- Each new conversation is declared wholly synthetic and remains separate from its analysis.
- Direct review confirms that the adversarial case contains an internal falsifier, the ambiguous case preserves two live branches, the relay case separates represented voices, and the runtime case preserves both office continuity and provenance discontinuity.
- Six fixtures validate, nine unit tests pass, skill validation passes, documentation validation reports no findings, and the clean-room scan returns no matches.

