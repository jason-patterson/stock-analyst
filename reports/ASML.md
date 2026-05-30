# ASML Holding N.V. (ASML) — Intrinsic Value Analysis

**Analysis Date:** May 30, 2026 | **Analyst:** AI Research Model | **Price at Analysis:** $1,612.76

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $1,612.76 |
| DCF Intrinsic Value (Base Case) | $528.44 |
| Upside / Downside | **−67.2%** |
| Analyst Consensus Target | $1,667.45 |
| Recommendation | **SELL / REDUCE (on valuation)** |
| Confidence | Medium |

**Thesis in one sentence:** ASML is the undisputed monopoly supplier of leading-edge lithography and one of the highest-quality businesses in the world, but at ~75x free cash flow and ~54x trailing earnings the current share price prices in flawless multi-decade execution, leaving the stock materially above any defensible discounted-cash-flow value.

---

## 2. Company Overview

ASML is the sole global supplier of extreme ultraviolet (EUV) lithography systems — the single most critical and irreplaceable tool in the manufacture of advanced (≤7nm) semiconductors. The company also dominates deep ultraviolet (DUV) immersion lithography and supplies metrology/inspection (YieldStar, HMI e-beam) and a large, high-margin Installed Base Management (service/upgrade) franchise. Its customers are the world's leading-edge foundries and memory makers — TSMC, Samsung, Intel, SK Hynix, and Micron. This is arguably the widest moat in technology: replicating EUV requires decades of R&D, a globally unique supply chain (Zeiss optics, Cymer light sources), and an installed base that locks in recurring service revenue.

Revenue streams divide into (1) **System sales** (EUV, DUV, and the emerging High-NA EUV platform priced at ~€350M+ per tool) and (2) **Installed Base Management** — service, parts and software upgrades that scale with the growing fleet and provide annuity-like recurring revenue with high margins. Operating margins of ~36% and a 52% return on equity reflect monopolistic pricing power and asset-light scaling.

**Key risks** are concentrated and severe: extreme customer concentration; deep cyclicality tied to the WFE (wafer fab equipment) capex cycle; binary geopolitical exposure (export controls restricting sales to China, historically ~20–40% of system shipments); lumpy revenue/FCF recognition tied to High-NA ramp timing; and valuation risk — the stock trades at a premium that leaves no margin of safety against any execution stumble.

---

## 3. Financial Snapshot

| Metric | TTM Value |
|--------|-----------|
| Revenue | $33.7B |
| EBITDA | $12.7B |
| Free Cash Flow | $8.24B |
| Net Income | $10.0B |
| FCF Margin | 24.5% |
| Revenue Growth YoY | 13.2% |
| Return on Equity | 52.2% |

**Commentary:** Earnings quality is excellent. FY2025 revenue of $32.7B grew from $21.2B in FY2022 — a ~15.5% three-year CAGR — while net income compounded ~19.6% over the same span (FY2022 $5.62B → FY2025 $9.61B). Operating margin of 36% and ROA of 15.7% underscore best-in-class profitability. The one nuance: TTM FCF ($8.24B) sits *below* net income ($10.0B), reflecting working-capital swings, customer-prepayment timing, and capex intensity ahead of the High-NA ramp. ASML's FCF is genuinely lumpy year-to-year, so any single-year FCF base understates or overstates "normalized" cash generation — an important caveat for the DCF below. The extreme P/B (>1,400x) and 13x debt-to-equity are artifacts of aggressive buybacks shrinking book equity, **not** signs of financial distress; the balance sheet is net cash ($8.4B cash vs. $2.7B debt).

---

## 4. Valuation — WACC Derivation

| Input | Value | Source / Rationale |
|-------|-------|--------------------|
| Risk-Free Rate (Rf) | 4.50% | 10-yr US Treasury |
| Equity Risk Premium (ERP) | 5.50% | Damodaran consensus |
| Beta (β) | 1.373 | Reported (semiconductor-equipment cyclicality) |
| Cost of Equity (Ke = Rf + β×ERP) | 12.05% | CAPM |
| Pre-tax Cost of Debt | 5.50% | Interest expense unavailable; high investment-grade fallback |
| Effective Tax Rate | 21.0% | Effective rate unavailable; standard fallback |
| After-tax Cost of Debt | 4.35% | 5.50% × (1 − 0.21) |
| Equity Weight (E/V) | 99.6% | $621.6B / ($621.6B + $2.7B) |
| Debt Weight (D/V) | 0.4% | Minimal leverage |
| **WACC** | **12.02%** | Equity-dominated; effectively cost of equity |

---

## 5. DCF Model

### Assumptions
| Assumption | Value | Rationale |
|------------|-------|-----------|
| Base FCF | $8.24B | TTM FCF. Note: below net income due to working-capital/timing; treated as conservative base. |
| Phase-1 Growth (yrs 1–5) | 18.0% | Blends 3-yr revenue CAGR (~15.5%), net income CAGR (~19.6%), and analyst near-term EPS growth (27–30%); tempered for High-NA capex intensity and cyclicality. |
| Phase-2 Growth (yrs 6–10) | 9.0% | ~50% of Phase-1, reflecting maturing fleet and slower marginal WFE expansion. |
| Terminal Growth Rate | 2.5% | Healthy global tech grower / GDP-plus proxy. |
| WACC | 12.02% | From Section 4. |

### 10-Year FCF Projection ($ millions)

| Year | Projected FCF | PV of FCF |
|------|--------------|-----------|
| 1 | $9,727 | $8,683 |
| 2 | $11,478 | $9,147 |
| 3 | $13,544 | $9,635 |
| 4 | $15,982 | $10,150 |
| 5 | $18,859 | $10,691 |
| 6 | $20,556 | $10,403 |
| 7 | $22,406 | $10,123 |
| 8 | $24,422 | $9,850 |
| 9 | $26,620 | $9,584 |
| 10 | $29,016 | $9,326 |

### Valuation Bridge
| Component | Value |
|-----------|-------|
| Sum of PV (FCFs) | $97.59B |
| PV of Terminal Value | $100.41B |
| Enterprise Value | $198.0B |
| (−) Total Debt | ($2.71B) |
| (+) Cash | $8.38B |
| Equity Value | $203.67B |
| Shares Outstanding | 0.385B |
| **Intrinsic Value / Share** | **$528.44** |
| Terminal Value % of EV | 50.7% |

**Interpretation:** The base-case DCF yields $528/share versus a $1,613 market price. The terminal value is a healthy 50.7% of EV (not over-reliant on perpetuity assumptions). The gap is enormous: to justify today's price purely on cash flows, the market must assume Phase-1 FCF growth far above 26% sustained for a decade *and/or* a WACC well below 10% — see the sensitivity table below, where even the most aggressive corner (26% growth, 10% WACC) reaches only $934.

---

## 6. Sensitivity Analysis — Intrinsic Value per Share

| Phase-1 Growth ↓ / WACC → | 10.0% | 11.0% | 12.02% | 13.0% | 14.0% |
|---------------------------|-------|-------|--------|-------|-------|
| **10%** | $504.96 | $440.69 | $389.42 | $349.85 | $316.68 |
| **14%** | $592.16 | $515.48 | $454.34 | $407.17 | $367.65 |
| **18% (base)** | $691.88 | $600.93 | **$528.44** | $472.55 | $425.75 |
| **22%** | $805.44 | $698.17 | $612.71 | $546.83 | $491.70 |
| **26%** | $934.27 | $808.41 | $708.17 | $630.93 | $566.31 |

Across the **entire** grid — spanning growth from 10% to 26% and WACC from 10% to 14% — the maximum intrinsic value is $934, still **~42% below** the current price. No reasonable DCF parameterization supports $1,613.

---

## 7. Relative Valuation

| Multiple | Company | Sector Avg (approx.) | Comment |
|----------|---------|------------|---------|
| P/E (TTM) | 53.8x | ~28–35x | Significant premium |
| Forward P/E | 33.8x | ~25x | Premium narrows on strong forward EPS, still rich |
| EV/EBITDA | 48.5x | ~20–25x | Roughly 2x sector |
| P/S | 18.4x | ~7–9x | Steep premium |
| P/B | 1,427x | n/m | Meaningless — buyback-distorted book equity |
| PEG | 2.41 | ~1.5–2.0 | Growth not cheap relative to rate |

ASML's premium to semi-cap peers (Applied Materials, Lam Research, KLA) is *partially* justified by its monopoly position and superior margins/ROE. But the multiples sit at roughly double sector norms, corroborating the DCF conclusion that valuation embeds near-perfect, long-duration execution.

---

## 8. Analyst Consensus

| Metric | Value |
|--------|-------|
| Mean Price Target | $1,667.45 |
| High Target | $2,006.53 |
| Low Target | $901.99 |
| Number of Analysts | 15 |
| Recommendation | Strong Buy (mean 1.45) |

**Note:** The consensus mean target ($1,667) sits essentially *at* the current price — implying the sell-side sees the stock as roughly fairly valued, with only ~3% upside. The wide range (low $902 to high $2,007) reflects substantial disagreement, and the low target is closer to (though still above) the DCF range. Sell-side targets here are largely momentum/multiple-anchored rather than intrinsic-cash-flow-anchored.

---

## 9. Investment Risks

**Bull Case (multiple-driven, +25%+ upside):**
- AI-driven structural demand sustains 20–30% revenue growth far longer than modeled, with High-NA EUV adding a multi-year second growth leg at premium ASPs.
- Monopoly pricing power and growing Installed Base service revenue lift FCF margins above the historical ~24%, raising normalized cash generation.
- Easing of China export restrictions or a sharp WFE up-cycle re-rates the stock; the market continues to award a scarcity premium to the only EUV supplier on earth.

**Bear Case (valuation/cyclical, −40% to −67% downside):**
- DCF base case ($528) and even the aggressive corner ($934) sit far below the current price — any growth disappointment or multiple compression toward historical/peer norms drives a severe de-rating.
- Geopolitical escalation (further China restrictions, Taiwan risk) cuts a major demand pool; semi cyclicality produces a sharp order/FCF air-pocket.
- High-NA ramp slips, customer capex digestion extends, or extreme customer concentration bites — and a 54x P/E offers zero margin of safety.

---

## 10. Verdict

**Recommendation: SELL / REDUCE on valuation — Medium confidence.** ASML is, without exaggeration, one of the finest businesses in the global economy: a genuine monopoly over the technology that enables all advanced computing, with 36% operating margins, 52% ROE, and a fortress net-cash balance sheet. There is nothing wrong with the *company*. The issue is entirely *price*. A disciplined two-stage DCF — using a generous 18% five-year FCF growth rate stepping to 9%, a 2.5% terminal rate, and a 12.0% WACC — produces an intrinsic value of **$528/share**, roughly one-third of the $1,613 market price. Critically, *no* cell in a sensitivity grid spanning 10–26% growth and 10–14% WACC exceeds $934, meaning the stock would need both heroic growth and an implausibly low discount rate simultaneously to be worth today's price on cash flows.

The disconnect between my DCF and the "Strong Buy" consensus is real and worth naming: sell-side targets (~$1,667 mean) are anchored to forward earnings multiples and AI-narrative momentum, not intrinsic cash flow. Two honest caveats temper the bearishness to *Medium* confidence: (1) ASML's FCF is genuinely lumpy, and a single-year TTM base of $8.24B may understate mid-cycle normalized cash generation (net income is already $10B); and (2) true monopolies with multi-decade visibility can rationally command premiums that standard DCF models structurally undervalue. Even allowing for both, the gap is too large to ignore.

**Price target range: $475–$710** (DCF base case bracketed by reasonable WACC/growth). **Catalysts to watch:** High-NA EUV order/shipment cadence, China export-control developments, the WFE capex cycle turn, and quarterly FCF normalization. **Time horizon:** 12–24 months. Long-term holders of a world-class compounder may reasonably choose to HOLD through cyclicality, but new capital deployed at $1,613 carries an unattractive risk/reward — we would wait for a meaningful pullback toward the $700–$900 zone before establishing a position.

---
*This analysis is for informational purposes only and does not constitute investment advice.*
---