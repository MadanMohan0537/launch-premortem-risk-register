from __future__ import annotations

from .models import LaunchBrief, Risk


def markdown_report(brief: LaunchBrief, risks: list[Risk], comparison: dict, intervention: dict) -> str:
    lines = [f"# {brief.name} premortem", "", brief.summary, "", "## Risk register", "", "| Score | Risk | Mechanism | Owner | Mitigation |", "|---:|---|---|---|---|"]
    for risk in sorted(risks, key=lambda r: (-r.score, r.title)):
        lines.append(f"| {risk.score} | {risk.title} | {risk.mechanism} | {risk.owner} | {risk.mitigation} |")
    lines += ["", "## Evaluation", "", f"- Human-list recall: {comparison['human_recall']}", f"- Risks novel to human list: {comparison['agent_risks_novel_to_human_list']}", f"- Assumption intervention targeted: {intervention['targeted']}", "", "> Generated risks are hypotheses for review, not predictions or professional advice."]
    return "\n".join(lines) + "\n"
