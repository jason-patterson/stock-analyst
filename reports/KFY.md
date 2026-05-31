# Korn Ferry (KFY) — Intrinsic Value Analysis

**Analysis Date:** May 30, 2026 | **Analyst:** AI Research Model | **Price at Analysis:** $69.98

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $69.98 |
| DCF Intrinsic Value | $100.81 |
| Upside / Downside | **+44.1%** |
| Analyst Consensus Target | $75.50 |
| Recommendation | **BUY** |
| Confidence | Medium |

**Thesis in one sentence:** Korn Ferry is a diversified, cash-generative organizational-consulting franchise trading at a modest ~12x forward earnings with a fortress net-cash balance sheet, where both a conservative DCF and a "strong buy" analyst consensus point to meaningful undervaluation, with cyclicality in staffing/recruiting being the principal risk to the upside case.

---

## 2. Company Overview

Korn Ferry is a global organizational consulting firm operating across five integrated solution lines: **Consulting** (talent strategy, organization design, leadership development), **Digital** (cloud HR platforms — Architect, Assess, Listen, Pay), **Executive Search**, **Professional Search & Interim**, and **Recruitment Process Outsourcing (RPO)**. This diversified model has progressively shifted the business away from purely transactional executive search toward higher-margin, more recurring advisory and software revenues, smoothing some — though not all — of the cyclicality inherent in talent markets.

The company's competitive moat rests on its proprietary intellectual property (assessment data on millions of professionals, leadership/compensation benchmarking databases), a globally recognized brand in executive search, and the cross-selling leverage of bundling search, consulting, and digital products into enterprise relationships. Switching costs are meaningful for embedded consulting and RPO engagements, and the data assets create a self-reinforcing flywheel that is difficult for smaller competitors to replicate.

**Key risks** are macro-cyclical: hiring volumes, executive search mandates, and consulting budgets all contract sharply in downturns, and a meaningful share of revenue remains fee-based and project-driven. The firm also competes against large strategy consultancies, boutique search firms, and HR-tech platforms, and carries integration risk from its historically acquisitive growth strategy.

---

## 3. Financial Snapshot

| Metric | TTM Value |
|--------|-----------|
| Revenue | $2.86B |
| EBITDA | $0.42B |
| Free Cash Flow | $0.29B |
| Net Income | $0.27B |
| FCF Margin | 10.2% |
| Revenue Growth YoY | 7.3% |
| Return on Equity | 14.3% |

**Commentary:** Earnings quality is solid — TTM operating cash flow ($373M) comfortably exceeds net income ($265M), and capex is light (~$60M/yr, ~2% of revenue), reflecting an asset-light, people-and-IP business. FCF has been lumpy across the cycle ($452M in FY2022 at the post-pandemic hiring peak, troughing to $229M in FY2024, recovering to $302M in FY2025; TTM $291M), underscoring the cyclical character of the franchise. The 4-year average FCF (~$314M) is broadly in line with the TTM figure. Margins are respectable for a services firm (9.4% net margin, 12.2% operating margin), and ROE of 14.3% on a lightly levered balance sheet is healthy. Critically, the company holds **$962M of cash against $565M of debt** — a net cash position of ~$398M — providing downside protection and optionality for buybacks, dividends, and tuck-in M&A.

---

## 4. Valuation — WACC Derivation

| Input | Value | Source / Rationale |
|-------|-------|--------------------|
| Risk-Free Rate (Rf) | 4.50% | 10-yr US Treasury |
| Equity Risk Premium (ERP) | 5.50% | Damodaran consensus |
| Beta (β) | 1.224 | Reported (KFY) |
| Cost of Equity (Ke = Rf + β×ERP) | 11.23% | CAPM |
| Pre-tax Cost of Debt | 5.50% | Fallback (investment-grade; interest expense not disclosed) |
| Effective Tax Rate | 21.0% | Fallback (effective rate not disclosed) |
| After-tax Cost of Debt | 4.35% | 5.50% × (1 − 0.21) |
| Equity Weight (E/V) | 86.5% | Mkt cap $3.63B / (3.63 + 0.56) |
| Debt Weight (D/V) | 13.5% | Debt $0.56B / EV base |
| **WACC** | **10.31%** | Weighted blend |

*Note: `interest_expense` and `effective_tax_rate` were not provided in the dataset. I applied the instructed investment-grade fallback cost of debt (5.5%) and statutory U.S. tax rate (21%). Given the small debt weight (13.5%), these assumptions have only a minor effect on the resulting WACC.*

---

## 5. DCF Model

### Assumptions
| Assumption | Value | Rationale |
|------------|-------|-----------|
| Base FCF | $291M | TTM FCF; close to 4-yr average (~$314M), avoiding the FY2022 cyclical peak |
| Phase-1 Growth (yrs 1–5) | 7.0% | Measured blend of ~7.3% revenue growth and ~8–9% analyst EPS growth, discounted for cyclicality |
| Phase-2 Growth (yrs 6–10) | 4.0% | ~57% of Phase-1, reflecting maturation toward GDP-plus |
| Terminal Growth Rate | 2.5% | Long-run nominal GDP proxy for a healthy U.S. grower |
| WACC | 10.31% | From CAPM derivation above |

### 10-Year FCF Projection ($ millions)

| Year | Projected FCF | PV of FCF |
|------|--------------|-----------|
| 1 | $312 | $283 |
| 2 | $334 | $274 |
| 3 | $357 | $266 |
| 4 | $382 | $258 |
| 5 | $409 | $250 |
| 6 | $425 | $236 |
| 7 | $442 | $223 |
| 8 | $460 | $210 |
| 9 | $478 | $198 |
| 10 | $497 | $187 |

### Valuation Bridge
| Component | Value |
|-----------|-------|
| Sum of PV (FCFs) | $2.38B |
| PV of Terminal Value | $2.45B |
| Enterprise Value | $4.83B |
| (−) Total Debt | ($0.56B) |
| (+) Cash | $0.96B |
| Equity Value | $5.23B |
| Shares Outstanding | 51.9M |
| **Intrinsic Value / Share** | **$100.81** |
| Terminal Value % of EV | 50.7% |

A terminal value of only ~51% of enterprise value is conservative (many DCFs exceed 70%), meaning the valuation is well-supported by near-/mid-term cash flows rather than distant perpetuity assumptions. The large net-cash position contributes meaningfully (~$8/share) to the per-share figure.

---

## 6. Sensitivity Analysis — Intrinsic Value per Share

| Phase-1 Growth ↓ / WACC → | 8.3% | 9.3% | 10.3% | 11.3% | 12.3% |
|---------------------------|------|------|-------|-------|-------|
| **3%** | $114.34 | $98.35 | $86.42 | $77.31 | $70.03 |
| **5%** | $124.06 | $106.47 | $93.36 | $83.35 | $75.35 |
| **7%** (base) | $134.52 | $115.20 | **$100.81** | $89.83 | $81.06 |
| **9%** | $145.74 | $124.57 | $108.81 | $96.77 | $87.17 |
| **11%** | $157.78 | $134.62 | $117.37 | $104.21 | $93.71 |

**Key insight:** Across all 25 scenarios — including the most punitive combination of 3% growth and a 12.3% WACC — intrinsic value ($70.03) lands at or above the current price of $69.98. The DCF therefore implies a wide margin of safety, with essentially no modeled scenario suggesting overvaluation.

---

## 7. Relative Valuation

| Multiple | Company | Comment |
|----------|---------|---------|
| P/E (TTM) | 13.9x | Below broad-market average; undemanding for a 14% ROE franchise |
| Forward P/E | 12.1x | Cheap relative to projected EPS growth (~8%); PEG ~1.2 |
| EV/EBITDA | 7.7x | Inexpensive; net cash flatters EV, understating cheapness |
| P/S | 1.27x | Reasonable for a services firm with 10%+ FCF margins |
| P/B | 1.80x | Modest given 14.3% ROE |

On every metric, KFY screens at the value end of the spectrum. The depressed EV/EBITDA (7.7x) is especially notable because the firm's $398M net-cash position compresses enterprise value — the operating business is being valued cheaply by the market.

---

## 8. Analyst Consensus

| Metric | Value |
|--------|-------|
| Mean Price Target | $75.50 |
| High Target | $84.00 |
| Low Target | $70.00 |
| Number of Analysts | 4 |
| Recommendation | Strong Buy (mean 1.4) |

The consensus mean target of $75.50 implies ~7.9% upside, and even the low target ($70.00) sits essentially at the current price — consistent with a favorable risk/reward skew. The "strong buy" rating (1.4 on a 1–5 scale) corroborates the directional thesis, though the small coverage universe (4–5 analysts) warrants some caution on consensus reliability.

---

## 9. Investment Risks

**Bull Case (+44% to intrinsic $100; +20% to high target $84):**
- Continued mix shift toward recurring consulting and digital/SaaS revenue lifts margins and FCF durability, compressing the cyclical discount.
- Net-cash balance sheet funds accretive buybacks (shares already only ~52M) and tuck-in M&A, compounding per-share value.
- A resilient labor/hiring backdrop sustains 7%+ revenue growth, driving the upper-half sensitivity scenarios ($108–$117/share).

**Bear Case (−10%+ if cycle turns and re-rating fails):**
- A macro/hiring downturn sharply contracts executive search and RPO volumes — FCF has historically swung from $452M to $229M peak-to-trough, illustrating earnings volatility.
- Fee-based, project-driven revenue offers limited visibility; a recession could push realized growth below the 3% bear-case row.
- Thin analyst coverage and small-cap liquidity risk could keep the valuation gap unclosed for an extended period (a "value trap" dynamic).

---

## 10. Verdict

**Recommendation: BUY** with a base-case price target of **$100** (DCF intrinsic value) and a 12-month working target range of **$84–$101**, anchored by the analyst high target on the conservative end and the DCF on the fundamental end. The investment case is unusually well-protected on the downside: every cell of the WACC × growth sensitivity grid resolves at or above the current $69.98 price, and the stock trades at just ~12x forward earnings and 7.7x EV/EBITDA despite a 14% ROE and a substantial net-cash position. The market appears to be over-penalizing KFY for the cyclicality of its staffing/search businesses while under-crediting the growing, higher-quality consulting and digital franchise.

The principal reason to demand patience rather than aggression is **cyclical timing**. Korn Ferry's cash flows can swing materially with the hiring cycle, and a labor-market downturn would temporarily depress FCF and could delay any re-rating. The thin (4–5 analyst) coverage also means the valuation discount may persist longer than fundamentals justify. Investors should size the position accordingly and view this as a 12–24 month thesis rather than a near-term catalyst trade.

**Catalysts to watch:** (1) quarterly fee-revenue and consulting/digital growth trends as evidence of mix-shift durability; (2) capital-return cadence (buyback pace given the net-cash hoard and ~3.1% dividend yield with a conservative 38% payout); (3) macro/hiring indicators and RPO pipeline commentary; and (4) any expansion of analyst coverage that could narrow the valuation gap. **Time horizon: 12–24 months.**

---
*This analysis is for informational purposes only and does not constitute investment advice.*
---