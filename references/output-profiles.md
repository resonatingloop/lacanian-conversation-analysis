# Output profiles v0.1

## Profile: `response/v0.1`

Use this profile by default. It is an evaluation in the assistant response, not a file bundle.

Return these sections in order:

1. **Scope and conditions** — supplied span, available structure, missing context, and quotation/privacy posture.
2. **Relational thesis** — one to three sentences naming the central interactional change.
3. **Sequence and phases** — the minimum phase map needed to support the thesis, with candidate boundaries and alternatives.
4. **Key claims** — each claim includes status, event references, evidence, downstream effect, and limitation.
5. **Lacanian warrant** — concepts actually used, what each distinguishes, and why its evidence threshold is met.
6. **Alternatives and counterevidence** — live rival accounts and inconvenient evidence.
7. **Adversarial pass** — the strongest way the preferred reading may be overfitting.
8. **Not established** — interior states, causality, durability, or missing-context claims the record cannot support.

Keep the response proportional to the trace. Do not manufacture claims to fill every section.

## Profile: `markdown-dossier/v0.1`

Use this profile when the user asks for a dossier, durable report, or reusable research artifact. Use the following section order exactly:

1. Title and profile declaration
2. Scope, trace, and privacy conditions
3. Relational thesis
4. Sequence and candidate phase boundaries
5. Relational geometry
6. Organizing signifiers
7. Rupture, failed repair, and effective repair
8. Claim ledger
9. Lacanian warrant
10. Alternatives and counterevidence
11. Adversarial pass
12. Limits and what is not established
13. Sources

The claim ledger uses this table shape:

| Claim ID | Proposition | Status | Event refs | Sequential evidence | Downstream effect | Concept/warrant | Counterevidence | Limit |
|---|---|---|---|---|---|---|---|---|

Allowed status values are `direct evidence`, `strong inference`, `plausible alternative`, and `speculation`.

The dossier is one Markdown document, not a required series of files. Return it inline unless file output is explicitly requested. If a destination is requested, write only the dossier and any separately requested machine-readable annotation; do not silently copy the source conversation beside it.

## Empty-section behavior

Do not invent content to make a dossier look complete. If a section is not supported, state in one sentence that the supplied trace does not establish it and identify the missing evidence.

## Quotation behavior

Use local event references throughout. Quote only what is needed for analysis. If the dossier may be public, prefer non-reconstructive paraphrase unless direct-quotation publication permission is explicit and case-specific.

