# Severity model

Two axes. The **tier** says whether a finding can be waived; the **priority** says how urgent it is.

| Tier | Meaning | Waivable | Blocks ship |
|---|---|---|---|
| Floor | Accessibility, truth, broken render, data loss | Never | Yes |
| Reflex | Slop defaults and craft errors | With a written waiver (below) | Until fixed or waived |
| Finish | Polish and preference | Not needed | No |

`info` is not a tier: it is a detector observation that becomes a finding only when it clusters (see look families in `data/look-families.yaml`).

## Mapping from source scales

| Source term | Becomes |
|---|---|
| Critical, P0, RED, Fatal, CRITICAL | Floor P0 |
| High, Major, P1, YELLOW, HIGH | Reflex P1 |
| Medium, Minor, MEDIUM | Reflex P2 |
| Low, Polish, Enhancement, Improvement, LOW | Finish P3 |

## Waivers

A Reflex finding is answered by a fix or a waiver. A waiver:

- names the rule id,
- gives a reason of at least 24 characters that cites the brief, the brand system or measured evidence,
- is not reused across rules.

Limits: at most 5 waivers per artifact. If the same rule is waived in 3 consecutive runs on one project, `learn` proposes it as house style for that project (the rule's profile override), and the waiver stops being needed.

## Ship condition

An artifact can ship when no Floor finding is open and every Reflex finding is fixed or waived.
