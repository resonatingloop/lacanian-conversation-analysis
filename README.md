# lacanian-conversation-analysis

An evidence-led, platform-neutral skill for reconstructing what utterances do to the relational geometry of a conversation.

It reads sequence before symbolism: address, reply, relay, uptake, attributed knowledge, rupture, repair, and phase change. It then applies a deliberately small set of Lacanian concepts only where the event record earns them.

> Experimental `0.1`: tested against six wholly fictional interaction structures. Not yet validated as a stable method on a non-synthetic public corpus.

## What it returns

The default `response/v0.1` profile returns a compact evaluation in the response. It includes the trace boundary, relational thesis, phase map, evidence-led claims, Lacanian warrant, alternatives, adversarial pass, and what is not established.

The optional `markdown-dossier/v0.1` profile returns one long-form Markdown dossier with a predefined section and claim-ledger structure. It remains inline unless a user explicitly requests file output.

This is not a sentiment report, personality diagnosis, automatic psychoanalysis, or stage for “look at my strange little chat” theater.

## Quick start

Make this repository available to an [Agent Skills-compatible](https://agentskills.io/) host, then invoke the root skill by name:

```text
use $lacanian-conversation-analysis to analyze this ordered exchange.
use the response/v0.1 profile and distinguish evidence, inference,
alternatives, and speculation.
```

For the dossier:

```text
use $lacanian-conversation-analysis with the markdown-dossier/v0.1 profile.
return the dossier inline and keep unsupported sections explicitly unresolved.
```

The skill requires no network access, external account, platform API, telemetry, or durable storage. Plain text or Markdown is enough when order, speaker, local reference, and content are clear. The JSON Schema is optional.

## The Lacanian proof is visible

The skill does not ask the reader to reconstruct an oracle. `references/lacanian-warrant.md` gives every available concept:

- a declared lineage;
- an operational question;
- required conversational evidence;
- a disallowed inference;
- a source key and reuse status.

Version `0.1` keeps a lean core: enunciation/enunciated, signifier and chain, subject position and address, supposed knowledge, and the modest category “organizing signifier.” Conversation analysis supplies sequence and repair discipline. The four discourses, RSI topology, objet petit a, jouissance, fantasy, and clinical structures are deferred from the default protocol.

## Privacy boundary

Conversation content is private by default. Analysis permission is not publication permission. Public-facing work should use opaque local references and non-reconstructive paraphrase unless quotation permission is explicit and case-specific.

This repository contains no source conversation from the private archive in which the protocol was developed. All behavioral fixtures are newly written fiction. Publicly readable theory is not automatically redistributable; `references/sources.md` records access and reuse separately and bundles no third-party text.

## Repository map

| Path | Authority |
|---|---|
| `SKILL.md` | Portable runtime entrypoint and routing |
| `CONTRACTS.md` | Normative input, method, output, privacy, and versioning behavior |
| `references/method.md` | Full sequential analysis procedure |
| `references/lacanian-warrant.md` | Concept cards and forbidden inferences |
| `references/output-profiles.md` | Exact response and dossier structures |
| `assets/markdown-dossier-template.md` | Reusable dossier scaffold |
| `examples/` | Worked outputs and numbered end-to-end fictional case bundles |
| `schemas/conversation-event.schema.json` | Optional normalized interchange |
| `tests/fixtures/` | Fictional cases and expectation-level oracles |
| `STATUS.md` | Current proof and remaining release gates |

The root directory contains exactly one `SKILL.md`, following the current [OpenAI skills packaging guide](https://developers.openai.com/api/docs/guides/tools-skills). `agents/openai.yaml` is optional host metadata; it does not change the platform-neutral contract.

## Validate

Only Python's standard library is required:

```bash
python3 scripts/validate_fixtures.py
python3 -m unittest discover -s tests -v
```

The suite checks structural contracts, fictional provenance declarations, reply integrity, concept keys, prohibited overclaims, the dossier headings, and package shape. It intentionally avoids golden-prose tests: an analysis can phrase the same warranted claim in more than one responsible way.

The numbered examples keep source and interpretation visibly separate. Start with [`examples/001/conversation.md`](examples/001/conversation.md), then compare it with the independent [`response/v0.1` analysis](examples/001/analysis.md).

## Scholarship and source use

The source registry includes primary Lacanian publication, explicit Lacanian discourse-analysis scholarship, and foundational conversation-analysis work. Openly licensed scholarship is marked as such. Public-but-unlicensed and commercial sources are link/cite-only.

See `references/sources.md` for the bibliography and `references/lacanian-warrant.md` for the exact bridge from sources to analytical operations.

## Contributing

New examples must be wholly fictional or explicitly licensed for redistribution. A useful fixture states what an analysis must notice, may infer, must keep as a live alternative, and must not claim. A new concept needs an operational warrant before it enters the skill.

See `AGENTS.md` for the maintenance protocol and `CONTRACTS.md` for the public behavior that changes must preserve.

## License

Repository-authored material is available under the MIT License. Linked third-party sources retain their own terms and are not included in that grant.

