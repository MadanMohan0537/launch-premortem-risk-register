# Evidence-driven backlog

Shipped mechanics and proposed hypotheses are deliberately separated.

| Priority | Feature | User problem and behavior | Dependencies | Success test | Risks and tradeoffs | Status |
|---|---|---|---|---|---|---|
| P1 | Assumption intervention round | Plausible risks do not reveal their causal premise. Toggle exactly one named assumption; compare mechanisms and scores while holding controls fixed. | Versioned briefs, stable personas | Blind review rates changed risks as tracking the changed assumption; deterministic fixture requires all four targeted rows to change and all four controls not to | Agents can invent causal links; mechanisms remain labeled hypotheses | Shipped |
| P2 | Risk falsification cards | Registers grow without a path to retire weak risks. Add cheapest disconfirming test, evidence threshold, deadline, and test-power note. | Register schema, owner workflow | More risks resolved per review-hour than plain register | Absence of evidence can be mistaken for safety | Planned |
| P2 | Persona distinctness audit | Personas collapse into the same generic voice. Score mechanism overlap and require unique private evidence. | Embeddings or token baseline, reviewed sample | Lower cross-persona redundancy without reducing documented-cause recall | Forced novelty may create noise | Planned |
| P2 | Evidence citation ledger | Reviewers cannot distinguish brief facts from generated claims. Attach each mechanism clause to brief evidence or mark it unsupported. | Source spans, claim parser | Seeded unsupported claims are all flagged with acceptable review load | Citation presence does not prove truth | Planned |
| P2 | Facilitation budget | More rounds may add repetition, not signal. Stop when marginal novel, actionable risk yield falls below a threshold. | Round-level novelty metric | Equal documented-cause recall with fewer review minutes | Early stopping can miss late minority concerns | Planned |
| P3 | Historical postmortem benchmark | Synthetic briefs do not prove usefulness. Evaluate frozen public incidents without leaking outcomes into prompts. | Curated public set, contamination protocol | Report documented-cause recall, novelty, reviewer precision, and denominators | Public accounts are incomplete and hindsight-biased | Planned |
| P3 | Power-balanced ownership | Moderator may assign every risk to engineering. Check ownership distribution and cross-functional dependencies. | Org-neutral role ontology | Reviewer-rated ownership improves without forced quotas | Quotas can misassign accountability | Planned |
| P3 | Dissent preservation | Merging can erase minority warnings. Keep provenance and a dissent appendix when confidence conflicts. | Merge provenance | Seeded minority risk remains inspectable after deduplication | More material increases review cost | Planned |
| P4 | Mitigation portfolio optimizer | Teams choose many overlapping mitigations. Select coverage under budget and dependency constraints. | Cost estimates, coverage graph | Higher reviewed risk coverage at equal budget than score-only ranking | False precision in cost and risk estimates | Planned |

Next slice: risk falsification cards. They convert a static register into a decision workflow without pretending the generated risks are predictions.
