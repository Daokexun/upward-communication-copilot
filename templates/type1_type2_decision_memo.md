# Type 1 vs. Type 2 Executive Decision Memo
> Grounded in Jeff Bezos's Decision Framework & Tencent WeChat Pay Product Governance.

## 1. Door Classification
- [ ] **Type 1 (One-Way Door)**: Irreversible, existential blast radius. Requires pre-mortem, 6-pager memo, and cross-VP consensus.
- [ ] **Type 2 (Two-Way Door)**: Reversible, fast iteration. Requires lightweight 1-pager, autonomous DRI execution, and exit triggers.

---

## 2. Executive Summary (BLUF)
- **Recommendation**: [State proposed decision in 1 sentence]
- **Resource Ask**: [Headcount, Cloud Budget $, Schedule Timeline]
- **Primary Business Delta**: [Quantified GMV, Latency ms, or Cost Reduction %]

---

## 3. Pre-Mortem Risk Analysis
*Assume it is 12 months from today and this initiative failed catastrophically. What caused the failure?*
1. **Failure Mode 1**: [Root cause] → **Mitigation**: [Pre-emptive architectural guardrail]
2. **Failure Mode 2**: [Root cause] → **Mitigation**: [Operational monitoring probe]

---

## 4. Reversibility & Two-Way Exit Criteria
- **Maximum Tolerable Loss**: If metric falls below [Threshold X] within [Y days], automated rollback triggers.
- **Exit Strategy**: Reverting back to legacy architecture requires [Z hours] with zero persistent data corruption.
