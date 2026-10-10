# Method and limitations

RiskCouncil uses fixed propose, rebut, and concede rounds. Each persona receives the same structured brief plus distinct private context. The moderator validates mechanisms, ownership, mitigations, score ranges, and removes near-duplicate titles only within the same assumption.

The shipped implementation is deterministic so experiments are reproducible and require no paid model. It demonstrates orchestration and evaluation mechanics, not the creative range of an LLM panel.

The P1 intervention changes only the audience assumption from a 100-customer pilot to a global 10,000-customer launch. Success is defined before execution: all four audience-linked mechanisms change, while all four support-model controls remain stable. This is a structural test; blind human ratings are planned and not claimed.

Important limitations:

- Generated risks are hypotheses, not forecasts, legal advice, or substitutes for affected experts.
- Token overlap is not a semantic gold standard and can misclassify paraphrases.
- Persona templates reflect their author's framing and can omit stakeholders.
- Synthetic briefs cannot establish real-world recall or reviewer value.
- Likelihood and impact scores are ordinal prompts for discussion, not calibrated probabilities.
- Human-baseline comparison is sensitive to wording and the completeness of the human list.
