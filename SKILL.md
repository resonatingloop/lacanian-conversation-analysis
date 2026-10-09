---
name: lacanian-conversation-analysis
description: Analyze ordered human, agent, or mixed conversations using evidence-led conversation analysis and selectively warranted Lacanian discourse concepts. Use for speaker position, address, signifiers, relay, rupture and repair, phase change, epistemic provenance, or a structured Markdown dossier. Do not use for generic summarization, sentiment scoring, personality diagnosis, or literary interpretation without an interactional question.
---

# Lacanian conversation analysis

Reconstruct what utterances do to the relational geometry of a conversation. Keep the enchantment answerable to the event record.

## Load the protocol

Before analysis:

1. Read `references/method.md`.
2. Read `references/lacanian-warrant.md` before using any Lacanian term.
3. Read `references/output-profiles.md` and select the requested profile. Default to `response/v0.1`.
4. Read `references/privacy-and-publication.md` when the material is private, the output may be saved or published, or direct quotation is contemplated.
5. Consult `references/sources.md` when explaining, defending, or extending a concept.

## Establish the input boundary

Accept ordered plain text, Markdown, or `conversation-event/v0.1` JSON. Do not require normalization when the supplied order, local references, speakers, and content are already clear.

State:

- what span was supplied;
- which structural fields are present;
- which important context is absent;
- whether the material is complete enough for sequence claims.

Never invent chronology, reply targets, provenance, participants, or missing turns.

## Analyze in passes

1. Reconstruct order, explicit replies, inferred address, relay, and uptake.
2. Mark changes in relational function even when the topic stays constant.
3. Compare candidate phases and locate the smallest evidence-supported boundaries.
4. Trace repair attempts through immediately subsequent turns.
5. Apply only concepts whose evidence requirements are met.
6. Build claims with event references and one of the four epistemic statuses.
7. Run the adversarial pass before rendering the result.

Distinguish local behavior in this exchange from a recurring participant pattern and from an effect produced by the room. Do not promote one into another without comparison evidence.

## Render

For `response/v0.1`, return the compact analysis in the response.

For `markdown-dossier/v0.1`, use the exact section order in `references/output-profiles.md`; `assets/markdown-dossier-template.md` is the writing scaffold. Return it inline unless the user explicitly requests a file and provides or accepts a destination.

Every result must separate observation, inference, alternatives, and speculation; name the concepts actually used; include counterevidence; and say what is not established.

## Runtime guarantees

This skill requires no network, external account, platform API, telemetry, or durable storage. Do not upload or persist conversation content merely because the host makes those capabilities available.

