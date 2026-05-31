# Alphabet Inc. (GOOG) — Intrinsic Value Analysis

**Analysis Date:** May 30, 2026 | **Analyst:** AI Research Model | **Price at Analysis:** $376.43

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $376.43 |
| DCF Intrinsic Value (base case) | $267.95 |
| Upside / Downside | **−28.8%** |
| Analyst Consensus Target | $414.74 |
| Recommendation | **HOLD** |
| Confidence | Medium |

**Thesis in one sentence:** Alphabet is a dominant, high-ROE cash machine, but at ~$376 the market is already capitalizing a successful AI-capex payoff that a conservative, normalized-FCF DCF does not support — leaving the stock fairly-to-fully valued with limited margin of safety.

---

## 2. Company Overview

Alphabet is the holding company for Google, operating through three reporting segments: **Google Services** (Search, YouTube, Android, Chrome, Play, devices, subscriptions), **Google Cloud**, and **Other Bets** (Waymo, Verily, etc.). Google Services — anchored by Search advertising and YouTube — remains the overwhelming profit engine, while Google Cloud has reached scale and turned profitable, providing a fast-growing second pillar. The company commands one of the widest competitive moats in technology: a dominant share of global search, the world's most-used mobile OS, two products with >2 billion users each, and a self-reinforcing data/AI flywheel.

Alphabet's competitive advantages are structural — network effects, scale economics in compute, proprietary data, and the Gemini AI model family integrated across the product stack. Revenue grew ~21.8% YoY to $422.5B (TTM), with a ~38% net margin and ~39% return on equity — exceptional metrics for a company of this size. The balance sheet is fortress-grade: ~$127B cash against ~$96B total debt (net cash positive), and an AAA-equivalent credit profile.

The central tension in the investment case is **capital intensity**. Alphabet is in the midst of a historic capex ramp ($91B in FY2025, accelerating further on a trailing-twelve-month basis to fund AI data centers and TPUs). This has temporarily compressed free cash flow even as net income surges. The bull case rests on these investments generating outsized future returns in Cloud and AI monetization; the bear case is that elevated capex becomes structural, depressing FCF conversion, just as generative-AI search disruption and regulatory/antitrust actions pressure the core.

---

## 3. Financial Snapshot

| Metric | TTM Value |
|--------|-----------|
| Revenue | $422.5B |
| EBITDA | $161.3B |
| Free Cash Flow (TTM, reported) | $27.9B |
| Free Cash Flow (FY2025, normalized) | $73.3B |
| Net Income | $160.2B |
| FCF Margin (normalized) | 18.2% |
| Revenue Growth YoY | 21.8% |
| Return on Equity | 38.9% |

**Commentary:** Top-line growth re-accelerated above 20%, and profitability is elite (operating margin 36%, net margin 38%). The headline issue is **FCF quality vs. timing**: reported TTM FCF of just $27.9B looks alarming next to $174B of operating cash flow, but it is an artifact of a peak capex cycle (~$146B annualized capex) tied to AI infrastructure. FY2025 full-year FCF of $73.3B is far more representative of run-rate cash generation, and I use it as the normalized DCF base. One caveat on earnings quality: TTM net income ($160.2B) grew ~82% YoY and exceeds reported EBITDA, suggesting non-operating/one-time gains inflate the trailing figure — I therefore anchor valuation on cash flow rather than peak earnings.

---

## 4. Valuation — WACC Derivation

| Input | Value | Source / Rationale |
|-------|-------|--------------------|
| Risk-Free Rate (Rf) | 4.50% | 10-yr US Treasury |
| Equity Risk Premium (ERP) | 5.50% | Damodaran consensus |
| Beta (β) | 1.27 | Reported (stock data) |
| Cost of Equity (Ke = Rf + β×ERP) | 11.47% | CAPM |
| Pre-tax Cost of Debt | 5.00% | Fallback for AAA-rated issuer (interest expense not disclosed); set below the 5.5% IG default given Alphabet's elite credit |
| Effective Tax Rate | 21.0% | Fallback (effective rate not disclosed); aligns with US statutory |
| After-tax Cost of Debt | 3.95% | 5.00% × (1 − 0.21) |
| Equity Weight (E/V) | 97.9% | $4,560.6B / ($4,560.6B + $95.9B) |
| Debt Weight (D/V) | 2.1% | Minimal leverage |
| **WACC** | **11.31%** | Equity-dominated capital structure |

---

## 5. DCF Model

### Assumptions
| Assumption | Value | Rationale |
|------------|-------|-----------|
| Base FCF | $73.3B | **Normalized to FY2025 FCF**, not TTM ($27.9B). TTM is distorted by a peak AI-capex cycle and would understate sustainable cash generation for a firm earning $160B net income. |
| Phase-1 Growth (yrs 1–5) | 12.0% | Below ~21% revenue growth and ~32% near-term EPS growth, deliberately discounted because elevated capex constrains FCF conversion through the investment cycle. |
| Phase-2 Growth (yrs 6–10) | 7.0% | Maturing growth as the law of large numbers and AI/search disruption temper expansion. |
| Terminal Growth Rate | 2.5% | Long-run nominal GDP proxy for a healthy mega-cap grower. |
| WACC | 11.31% | From Section 4. |

### 10-Year FCF Projection ($ millions)

| Year | Projected FCF | PV of FCF |
|------|--------------|-----------|
| 1 | $82,058 | $73,720 |
| 2 | $91,905 | $74,177 |
| 3 | $102,933 | $74,637 |
| 4 | $115,285 | $75,100 |
| 5 | $129,120 | $75,565 |
| 6 | $138,158 | $72,639 |
| 7 | $147,829 | $69,827 |
| 8 | $158,177 | $67,123 |
| 9 | $169,250 | $64,524 |
| 10 | $181,097 | $62,025 |

### Valuation Bridge
| Component | Value |
|-----------|-------|
| Sum of PV (FCFs) | $709.3B |
| PV of Terminal Value | $721.6B |
| Enterprise Value | $1,431.0B |
| (−) Total Debt | ($95.9B) |
| (+) Cash | $126.8B |
| Equity Value | $1,461.9B |
| Shares Outstanding | 5.456B |
| **Intrinsic Value / Share** | **$267.95** |
| Terminal Value % of EV | 50.4% |

The TV contributes a moderate ~50% of EV (healthy — not overly back-loaded). The base case implies the stock is ~29% above intrinsic value at a normalized FCF base.

---

## 6. Sensitivity Analysis — Intrinsic Value per Share

Rows = Phase-1 FCF growth; Columns = WACC. **Current price: $376.43.**

| Phase-1 Growth ↓ / WACC → | 9.3% | 10.3% | 11.3% (base) | 12.3% | 13.3% |
|---------------------------|------|-------|--------------|-------|-------|
| 7%  | $288.55 | $249.63 | $219.70 | $196.00 | $176.79 |
| 9.5% | $319.95 | $276.33 | $242.79 | $216.24 | $194.73 |
| **12% (base)** | $354.21 | $305.44 | **$267.95** | $238.28 | $214.25 |
| 14% | $391.52 | $337.12 | $295.31 | $262.24 | $235.47 |
| 17% | $432.09 | $371.54 | $325.03 | $288.25 | $258.48 |

**Interpretation:** The current price of ~$376 is only reached under optimistic combinations — e.g., ≥14% sustained FCF growth paired with a sub-10% WACC, or ~17% growth at ~10.3% WACC. Across the central region of the grid, intrinsic value clusters in the **$240–$305** range. The market is effectively pricing the upper-left (bull) corner.

---

## 7. Relative Valuation

| Multiple | Company | Mega-Cap Tech Ref. | Comment |
|----------|---------|--------------------|---------|
| P/E (TTM) | 28.7x | ~28–30x | In line; flattered by one-off TTM earnings |
| Forward P/E | 26.0x | ~25–27x | Fairly valued vs. peers |
| EV/EBITDA | 28.1x | ~18–20x | Elevated; rich on a cash-flow-to-EV basis |
| P/S | 10.8x | ~7–9x | Premium to peer group |
| P/B | 9.5x | ~9–11x | In line for an asset-light, high-ROE compounder |
| PEG | 1.48 | ~1.5–2.0 | Reasonable given growth |

On forward earnings GOOG screens fairly valued versus mega-cap peers, but on EV/EBITDA and P/S it carries a premium. The PEG of ~1.5 is defensible given a ~20%+ growth profile and best-in-class returns on capital.

---

## 8. Analyst Consensus

| Metric | Value |
|--------|-------|
| Mean Price Target | $414.74 |
| High Target | $460.00 |
| Low Target | $285.00 |
| Number of Analysts | 15 |
| Recommendation | Strong Buy (mean 1.43) |

Sell-side is decidedly bullish (Strong Buy), with a mean target ~10% above the current price and ~55% above my base-case DCF. The wide gap reflects the Street's confidence that AI investments will convert to accelerating FCF — a more optimistic view than my normalized, WACC-discounted model supports.

---

## 9. Investment Risks

**Bull Case (+15–22% upside, toward $432–$460):**
- AI-capex cycle pays off: Cloud margins expand and Gemini-driven Search/ads monetization re-accelerates revenue, lifting FCF growth toward 14–17% as capex intensity normalizes.
- Operating leverage drives FCF conversion sharply higher once the data-center build-out plateaus, validating the Street's $415+ targets.
- Waymo/Other Bets or a re-rating on AI leadership provides optionality not in the base case.

**Bear Case (−25 to −40% downside, toward $200–$240):**
- Capex stays structurally elevated, permanently depressing FCF conversion below historical norms.
- Generative-AI disruption erodes the high-margin Search query/ad franchise; antitrust remedies (ad-tech, default-search) impair the core business model.
- Multiple compression: a 28x EV/EBITDA is vulnerable if growth decelerates or rates stay higher-for-longer (WACC ≥12.3% pushes value to ~$215–$238).

---

## 10. Verdict

**Recommendation: HOLD.** My base-case DCF, anchored to normalized FY2025 FCF of $73.3B and a CAPM-derived 11.31% WACC, produces an intrinsic value of **$267.95** — roughly 29% below the current $376 price. The sensitivity table reinforces this: the prevailing price is only justified under genuinely optimistic assumptions (≥14% durable FCF growth and/or a sub-10% discount rate). My fair-value range is **$240–$305**, centered well below where the stock trades today.

That said, this is a "great company, full price" situation rather than a broken thesis. Alphabet's franchise quality — ~39% ROE, 36% operating margins, net-cash balance sheet, and three of the most valuable digital platforms on earth — is undeniable, and the single largest swing factor (the AI-capex payoff) is precisely what a conservative FCF model cannot yet credit. If capex intensity moderates and Cloud/AI monetization converts into accelerating free cash flow, the bull case toward the analyst consensus of ~$415 becomes very achievable, and the normalized FCF base I used would prove too low.

**Action:** Existing holders should hold; the secular story and balance-sheet strength argue against selling a compounder of this caliber. New capital should await a better entry — ideally a pullback toward the **$300–$320** zone — which would restore a margin of safety. **Catalysts to watch:** quarterly capex trajectory and FCF conversion, Cloud operating margins, Search ad-revenue resilience against AI substitution, and antitrust/regulatory rulings. **Time horizon:** 12–24 months.

---
*This analysis is for informational purposes only and does not constitute investment advice.*
---