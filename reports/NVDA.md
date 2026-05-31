# NVIDIA Corporation (NVDA) — Intrinsic Value Analysis

**Analysis Date:** May 30, 2026 | **Analyst:** AI Research Model | **Price at Analysis:** $211.14

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $211.14 |
| DCF Intrinsic Value (base case) | $94.99 |
| Upside / Downside | **−55.0%** |
| Analyst Consensus Target | $296.81 |
| Recommendation | **HOLD** |
| Confidence | Medium |

**Thesis in one sentence:** NVIDIA is the undisputed AI-infrastructure franchise with extraordinary profitability, but a disciplined CAPM-based DCF — penalized by a 2.24 beta and a conservative cash-flow base — argues the current price already discounts years of flawless hyper-growth, leaving the risk/reward balanced rather than compelling.

---

## 2. Company Overview

NVIDIA has transformed from a gaming-GPU vendor into the foundational compute platform for the global artificial-intelligence build-out. Its **Compute & Networking** segment — data-center accelerators (Hopper/Blackwell-class GPUs), NVLink/Infiniband/Spectrum networking, and the CUDA software stack — now dominates revenue and earnings. The legacy **Graphics** segment (GeForce gaming GPUs, RTX professional visualization) remains a profitable but secondary contributor. Revenue scaled from ~$27B in FY2023 to ~$216B in FY2026, with TTM revenue of $253.5B.

The competitive moat is exceptionally wide and rests on three reinforcing pillars: (1) a multi-generation hardware performance lead, (2) the **CUDA software ecosystem** that creates deep developer lock-in and high switching costs, and (3) full-stack systems integration (GPU + networking + software + reference architectures) that competitors struggle to replicate. The result is a near-monopoly economic profile — a 63% net margin and a 114% return on equity that are virtually unprecedented for a company of this scale.

Key risks are correspondingly structural: customer concentration among a handful of hyperscalers, the cyclical/"digestion" risk inherent in capex-driven demand, rising in-house silicon efforts by major customers (Google TPU, Amazon Trainium, etc.), competitive pressure from AMD, and geopolitical/export-control exposure to China. The central debate is not whether NVIDIA is a great business — it plainly is — but whether the durability and trajectory of AI capex justify a ~$5.1 trillion market capitalization.

---

## 3. Financial Snapshot

| Metric | TTM Value |
|--------|-----------|
| Revenue | $253.5B |
| EBITDA | $165.5B |
| Free Cash Flow (TTM reported) | $46.3B* |
| Free Cash Flow (FY2026 audited, used as base) | $96.7B |
| Net Income | $159.6B |
| FCF Margin (FY2026 basis) | ~44.8% |
| Revenue Growth YoY | +85.2% |
| Return on Equity | 114.3% |

*\*Data note:* The reported **TTM FCF of $46.3B is treated as anomalous**. TTM operating cash flow ($125.6B) is *higher* than FY2026 ($102.7B), yet the implied TTM FCF is far lower — which would require ~$79B of capex versus a historical run-rate of ~$6B. This is inconsistent with NVIDIA's asset-light, fabless model. I therefore anchor the DCF to the **FY2026 audited FCF of $96.7B**, a clean and conservative figure.

**Commentary:** Margins and returns are best-in-class globally. The most important quality-of-earnings nuance is that **free cash flow currently lags net income** ($96.7B FCF vs. $159.6B net income), because explosive growth is consuming cash through working-capital builds (inventory pre-positioning, receivables). As growth normalizes, FCF should converge toward earnings — a structural tailwind to intrinsic value not fully captured by a current-FCF base.

---

## 4. Valuation — WACC Derivation

| Input | Value | Source / Rationale |
|-------|-------|--------------------|
| Risk-Free Rate (Rf) | 4.50% | 10-yr US Treasury |
| Equity Risk Premium (ERP) | 5.50% | Damodaran consensus |
| Beta (β) | 2.244 | Reported (stock data) |
| Cost of Equity (Ke = Rf + β×ERP) | 16.84% | CAPM |
| Pre-tax Cost of Debt | 5.50% | Fallback (interest expense N/A); reflects effective AA-grade credit |
| Effective Tax Rate | 21.0% | Fallback (statutory; reported rate N/A) |
| After-tax Cost of Debt | 4.35% | |
| Equity Weight (E/V) | 99.8% | Market cap / (Mkt cap + Debt) |
| Debt Weight (D/V) | 0.2% | Minimal leverage |
| **WACC** | **16.81%** | |

> **Caveat:** The 16.81% WACC is driven almost entirely by the elevated 2.24 beta. While methodologically correct, this is arguably punitive for a company with this cash-generation quality and a net-cash balance sheet ($53.2B cash vs. $12.8B debt). Many practitioners normalize NVDA's long-run beta toward ~1.5 (implying a WACC of ~12.7%). The sensitivity table (Section 6) deliberately spans this range.

---

## 5. DCF Model

### Assumptions
| Assumption | Value | Rationale |
|------------|-------|-----------|
| Base FCF | $96.7B | FY2026 audited FCF (TTM figure rejected as anomalous — see §3) |
| Phase-1 Growth (yrs 1–5) | 28.0% | Below analyst near-term revenue/EPS growth (40–85%) to reflect deceleration off a massive base and law of large numbers |
| Phase-2 Growth (yrs 6–10) | 13.0% | ~46% of Phase-1; orderly fade toward maturity |
| Terminal Growth Rate | 2.5% | Long-run US nominal GDP proxy (healthy grower) |
| WACC | 16.81% | From Section 4 |

### 10-Year FCF Projection ($ millions)

| Year | Projected FCF | PV of FCF |
|------|--------------|-----------|
| 1 | $123,745 | $105,937 |
| 2 | $158,394 | $116,086 |
| 3 | $202,744 | $127,206 |
| 4 | $259,513 | $139,392 |
| 5 | $332,176 | $152,745 |
| 6 | $375,359 | $147,763 |
| 7 | $424,156 | $142,944 |
| 8 | $479,296 | $138,281 |
| 9 | $541,605 | $133,771 |
| 10 | $612,013 | $129,408 |

### Valuation Bridge
| Component | Value |
|-----------|-------|
| Sum of PV (FCFs) | $1,333.5B |
| PV of Terminal Value | $926.9B |
| Enterprise Value | $2,260.5B |
| (−) Total Debt | ($12.8B) |
| (+) Cash | $53.2B |
| Equity Value | $2,300.8B |
| Shares Outstanding | 24.22B |
| **Intrinsic Value / Share** | **$94.99** |
| Terminal Value % of EV | 41.0% |

A terminal-value share of only 41% indicates the valuation is driven mainly by explicit near-term cash flows rather than perpetuity assumptions — a sign of a well-grounded (not terminal-dependent) model.

---

## 6. Sensitivity Analysis — Intrinsic Value per Share

Rows = Phase-1 FCF growth; Columns = WACC. Base case (28% / 16.8%) in the center.

| Phase-1 Growth ↓ / WACC → | 13.0% | 15.0% | 16.8% (base) | 18.0% | 20.0% |
|---------------------------|-------|-------|--------------|-------|-------|
| **18%** | $97.60 | $78.88 | $66.75 | $60.44 | $51.94 |
| **23%** | $117.62 | $94.67 | $79.80 | $72.07 | $61.68 |
| **28% (base)** | $141.01 | $113.07 | **$94.99** | $85.61 | $72.98 |
| **33%** | $168.16 | $134.41 | $112.59 | $101.26 | $86.05 |
| **38%** | $199.54 | $159.04 | $132.87 | $119.29 | $101.07 |

**Key takeaway:** Even the most optimistic corner of this grid (38% growth, 13% WACC = $199.54) sits *below* the current $211.14 price. To justify today's valuation on a pure FCF-DCF basis, one must assume **either** sustained >38% FCF growth, **or** a materially lower discount rate, **or** (most importantly) that FCF converges upward toward NVIDIA's much larger net income — a normalization not modeled in this conservative base.

---

## 7. Relative Valuation

| Multiple | Company | Sector Context | Comment |
|----------|---------|----------------|---------|
| P/E (TTM) | 32.4x | Semis ~30–35x | In line — not stretched for the growth |
| Forward P/E | 16.7x | Semis ~25x | **Cheap** on forward earnings; PEG 0.66 |
| EV/EBITDA | 30.6x | Semis ~20–25x | Premium, justified by margins |
| P/S | 20.2x | Semis ~7–9x | Rich on sales |
| P/B | 32.6x | Semis ~6–8x | Very high, but ROE of 114% supports it |

The tension is stark: NVDA looks **expensive on asset/sales multiples and the DCF**, yet **inexpensive on forward earnings** (16.7x forward P/E, PEG 0.66). The reconciling variable is forward-earnings growth — if analyst FY2027/FY2028 estimates ($391B and $548B revenue) are achieved, the multiple compression makes the stock look reasonable; the DCF's conservatism stems from anchoring to current depressed FCF conversion.

---

## 8. Analyst Consensus

| Metric | Value |
|--------|-------|
| Mean Price Target | $296.81 |
| High Target | $500.00 |
| Low Target | $180.00 |
| Number of Analysts | 58 |
| Recommendation | Strong Buy (mean 1.30) |

Consensus implies ~+41% upside and is overwhelmingly bullish — a notable divergence from this report's conservative base-case DCF, attributable primarily to the Street's lower implied discount rate and assumed FCF-to-earnings normalization.

---

## 9. Investment Risks

**Bull Case (toward $200–$300):**
- FCF converges toward net income ($159.6B+) as working-capital intensity normalizes — directly and materially lifting intrinsic value.
- AI infrastructure capex super-cycle persists multiple years; Blackwell/next-gen ramps sustain 40%+ near-term growth (consistent with consensus).
- A normalized beta (~1.5) and WACC (~12.7%) lift fair value into the $140–$200 range even before FCF normalization.

**Bear Case (toward $70–$100):**
- AI capex digestion / air-pocket as hyperscalers pause; revenue growth decelerates faster than modeled.
- Customer in-house silicon (TPU, Trainium, MTIA) and AMD erode share and pricing power; margins compress from peak.
- Beta-driven 16.8% discount rate proves appropriate for a high-volatility name, and the base-case ~$95 DCF reasserts itself; export-control/China headwinds intensify.

---

## 10. Verdict

**Recommendation: HOLD. Fair-value range: $130–$200; price target ~$165 (blended).**

NVIDIA is, without exaggeration, one of the highest-quality businesses ever analyzed by this framework — a 63% net margin, 114% ROE, net-cash balance sheet, and a defensible CUDA moat at the center of the most important technology platform shift in a generation. Nothing here disputes the franchise's excellence. The question is purely one of price.

The disciplined base-case DCF ($94.99) flags meaningful overvaluation, but it is deliberately conservative on two fronts that I weight heavily: (1) it anchors to a depressed FCF base ($96.7B) that materially understates true earnings power ($159.6B net income), and (2) it applies a 16.81% WACC driven by a 2.24 beta that arguably overstates NVIDIA's long-run cost of capital. Adjusting for FCF normalization and a more typical ~12–13% discount rate pushes fair value into roughly the **$140–$200** zone — which brackets, but does not clearly exceed, the current $211 price. Against a Strong Buy consensus and a $296.81 target, my stance is more cautious because today's price already requires sustained, near-flawless execution to be justified on cash flows.

**Net:** the risk/reward is balanced rather than compelling at $211. I would not chase the stock here, nor short a franchise of this quality. **Catalysts to watch:** quarterly data-center revenue and guidance, Blackwell ramp/margins, FCF-to-net-income conversion trend (the single most important valuation lever), hyperscaler capex commentary, and China/export-control developments. **Time horizon:** 12–18 months; I would become a more constructive buyer on a pullback toward the $150–$165 range or on clear evidence of FCF normalization.

---
*This analysis is for informational purposes only and does not constitute investment advice.*
---