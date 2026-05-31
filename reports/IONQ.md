# IonQ, Inc. (IONQ) — Intrinsic Value Analysis

**Analysis Date:** May 30, 2026 | **Analyst:** AI Research Model | **Price at Analysis:** $72.07

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $72.07 |
| Intrinsic Value (probability-weighted, EV/Revenue method) | **~$23.00** |
| Intrinsic Value Range (bear–bull) | $11.70 – $35.70 |
| Upside / Downside | **−68%** |
| Analyst Consensus Target | $67.64 |
| Recommendation | **SELL** (on valuation) |
| Confidence | **Low** (binary, narrative-driven outcome) |

**Thesis in one sentence:** IonQ is a genuine technology leader in trapped-ion quantum computing with a fortress balance sheet ($2.0B net cash), but at 133× EV/revenue and 144× sales the stock already discounts a near-flawless decade of commercialization — leaving the fundamental risk/reward heavily skewed to the downside even under generously bullish scenarios.

> **Important framing:** A conventional FCF-DCF is *not applicable* here. Free cash flow has been negative every year (-$57M → -$300M, 2022–2025) and is worsening, and EBITDA is deeply negative (-$662M TTM). The reported "positive" TTM net income of $308M is **non-operational** (operating margin is −402%) — it reflects non-cash fair-value gains, not earnings power. Valuation therefore rests on a forward **EV/Revenue** framework discounted at WACC.

---

## 2. Company Overview

IonQ, Inc. develops and commercializes quantum computing systems based on **trapped-ion technology**, widely regarded as one of the higher-fidelity architectures in the field. The company sells access to its quantum computers by qubit capacity, both directly and through major cloud platforms — Amazon Braket (AWS), Microsoft Azure Quantum, and Google Cloud Marketplace — alongside its own cloud service. It also pursues adjacent opportunities in quantum-safe networking/communications and quantum sensing/detection, and earns revenue from hardware sales, maintenance/support, and co-development consulting contracts.

The investment narrative is built on **optionality**: quantum computing addresses a potentially enormous long-term TAM (drug discovery, materials science, optimization, cryptography). IonQ's moat, to the extent one exists, derives from technical IP, qubit fidelity leadership, talent, and entrenchment within the hyperscaler cloud ecosystems. However, the commercial market remains nascent — FY2025 revenue was just $130M — and competition is formidable, spanning well-capitalized incumbents (IBM, Google, Microsoft, Honeywell/Quantinuum) and superconducting/photonic/neutral-atom rivals whose architectures could ultimately win.

**Key risks** are existential and binary in nature: the timeline to fault-tolerant, commercially indispensable quantum advantage is uncertain and could slip many years; a competing modality could render trapped-ion approaches uncompetitive; and the company is years from cash-flow breakeven, funding operations from its balance sheet. The $2.0B cash pile (raised via equity, which dilutes holders) is the company's most important asset today.

---

## 3. Financial Snapshot

| Metric | TTM / Latest Value |
|--------|-----------|
| Revenue (TTM) | $0.19B |
| Revenue (FY2025) | $0.13B |
| EBITDA (TTM) | −$0.66B |
| Free Cash Flow (TTM) | −$0.09B |
| Operating Cash Flow (TTM) | −$0.40B |
| Net Income (TTM, GAAP) | +$0.31B *(non-operational)* |
| FCF Margin | −48.8% |
| Revenue Growth (FY2024→FY2025) | +202% |
| Operating Margin | −402% |
| Cash & Equivalents | $2.03B |
| Total Debt | $0.03B |

**Commentary.** Revenue growth is explosive off a tiny base ($11M → $22M → $43M → $130M, 2022–2025), and consensus sees ~$269M in FY2026 (+107%) and ~$389M in FY2027 (+45%). But the **quality of earnings is poor**: the headline positive net income is an accounting artifact (warrant/derivative remeasurement), while *operating* losses are widening (EBIT −$634M in FY2025) and the cash burn is accelerating (operating cash flow −$283M, FCF −$300M in FY2025). The company is not remotely self-funding; it is converting its equity-raised cash balance into R&D and capacity. Dilution risk is therefore a recurring feature. The redeeming feature is the balance sheet — $2.0B net cash provides a long runway (several years at current burn).

---

## 4. Valuation — WACC Derivation

| Input | Value | Source / Rationale |
|-------|-------|--------------------|
| Risk-Free Rate (Rf) | 4.50% | 10-yr US Treasury |
| Equity Risk Premium (ERP) | 5.50% | Damodaran consensus |
| Beta (β) | 3.05 | Reported; reflects extreme volatility of a speculative name |
| Cost of Equity (Ke = Rf + β×ERP) | 21.29% | CAPM |
| Pre-tax Cost of Debt | 6.50% | Fallback (no interest data; speculative credit) |
| Effective Tax Rate | 21.0% | Fallback (no meaningful taxes; pre-profit) |
| After-tax Cost of Debt | 5.14% | |
| Equity Weight (E/V) | 99.9% | Debt is negligible ($30M) |
| Debt Weight (D/V) | 0.1% | |
| **WACC** | **21.27%** | ≈ cost of equity given all-equity structure |

A 21.3% discount rate appropriately reflects the company's risk: a 3.05 beta, pre-revenue-scale operations, cash burn, and binary commercialization outcomes.

---

## 5. Valuation — Forward EV/Revenue Model (DCF not applicable)

### Why not a standard DCF?
Base FCF is **negative (−$91M TTM)** and has deteriorated every year; the 4-year average FCF (−$143M) is also negative. A two-stage FCF-DCF cannot produce a meaningful intrinsic value from a negative, worsening base. EV/EBITDA is likewise unusable (EBITDA −$662M). I therefore value IonQ on a **forward EV/Revenue** basis: project revenue to FY2030, apply a normalized exit multiple, discount the terminal enterprise value to present at the 21.27% WACC, and bridge to equity with net cash.

### Revenue Projection ($ millions)

| Fiscal Year | Projected Revenue | YoY Growth | Source / Rationale |
|------|--------------|------|--------------------|
| 2025 (actual) | $130 | +202% | Reported |
| 2026E | $269 | +107% | Analyst consensus (10 analysts) |
| 2027E | $389 | +45% | Analyst consensus (13 analysts) |
| 2028E | $545 | +40% | Modeled taper |
| 2029E | $736 | +35% | Modeled taper |
| 2030E | $957 | +30% | Modeled taper |

### Base-Case Valuation Bridge

| Component | Value |
|-----------|-------|
| FY2030E Revenue | $957M |
| Exit EV/Revenue multiple (base) | 12.0× |
| Terminal Enterprise Value (FY2030) | $11.48B |
| Discount factor @ 21.27% over ~4.5 yrs | 0.420 |
| PV of Terminal Enterprise Value | $4.82B |
| (+) Net Cash (cash $2.03B − debt $0.03B) | $2.00B |
| Equity Value | $6.82B |
| Shares Outstanding | 373.3M |
| **Base-Case Intrinsic Value / Share** | **$18.28** |

A 12× forward EV/Revenue exit multiple is already generous for a company at ~$1B revenue scale; it implies the market still richly rewards growth in 2030. Even so, the base case lands **~75% below** the current price.

### Scenario Summary

| Scenario | FY2030 Revenue | Exit EV/Rev | Intrinsic Value / Share | Prob. |
|----------|---------------|-------------|------------------------|-------|
| Bear | $700M | 8× | $11.70 | 30% |
| Base | $957M | 12× | $18.28 | 40% |
| Bull | $1,500M | 18× | $35.72 | 25% |
| Hyper-Bull | $2,500M | 22× | $67.20 | 5% |
| **Probability-Weighted** | — | — | **~$23.00** | 100% |

**Read-through:** Only the *hyper-bull* case (≥$2.5B revenue in 2030 — a ~6.4× increase from 2027 consensus — *and* a still-rich 22× exit) approaches today's price. The market is pricing the tail outcome as the base case.

---

## 6. Sensitivity Analysis — Intrinsic Value per Share

PV per share = (FY2030 Revenue × Exit Multiple × 0.420 + $2.0B net cash) ÷ 373.3M shares. Discount rate = 21.27% WACC over ~4.5 years.

| FY2030 Revenue ↓ / Exit EV/Rev → | 8× | 12× | 15× | 18× | 22× |
|---|---|---|---|---|---|
| **$700M** | $11.66 | $14.81 | $17.17 | $19.54 | $22.69 |
| **$957M** | $13.98 | **$18.28** | $21.51 | $24.74 | $29.04 |
| **$1,250M** | $16.61 | $22.24 | $26.45 | $30.67 | $36.29 |
| **$1,500M** | $18.86 | $25.61 | $30.67 | $35.73 | $42.48 |
| **$2,000M** | $23.36 | $32.36 | $39.11 | $45.85 | $54.85 |

Every cell in a broad, plausible grid sits **below the $72.07 market price**. To justify the current price requires *both* revenue materially above $2.5B in 2030 *and* a sustained premium exit multiple — i.e., near-flawless execution priced as the central case.

---

## 7. Relative Valuation

| Multiple | Company | Comment |
|----------|---------|---------|
| P/E (TTM) | 184.8× | Meaningless — driven by non-operating net income |
| Forward P/E | −69.1× | Negative — company is loss-making forward |
| EV/EBITDA | −37.6× | Negative EBITDA — not usable |
| EV/Revenue (TTM) | 133.1× | Extreme; vs. high-growth software norms of ~10–20× |
| P/S (TTM) | 143.8× | Among the richest in the entire market |
| P/B | 5.4× | The only "normal-looking" multiple — but book is dominated by cash |

On every revenue/sales-based metric, IonQ trades at a multiple roughly **6–10× richer** than even premium hyper-growth software peers, despite being pre-profitability with a still-tiny revenue base.

---

## 8. Analyst Consensus

| Metric | Value |
|--------|-------|
| Mean Price Target | $67.64 |
| High Target | $100.00 |
| Low Target | $44.78 |
| Number of Analysts | 13 |
| Recommendation | Strong Buy (1.38 mean) |

**Disconnect noted:** Sell-side consensus is "Strong Buy" with a $67.64 mean target (roughly the current price). This reflects a thematic/momentum-driven framework and revenue-multiple-on-future-revenue logic rather than discounted cash returns. My fundamental work shows the price embeds extraordinary expectations; investors should weigh that the consensus target offers ~0% upside and is not anchored to cash-flow value.

---

## 9. Investment Risks

**Bull Case (path toward $35–$67+):**
- Quantum advantage inflects commercially sooner than expected; enterprise/government demand scales revenue past $1.5–2.5B by 2030.
- IonQ's trapped-ion fidelity lead and hyperscaler distribution translate into durable share and premium pricing.
- $2.0B cash funds the roadmap to scale without distressed dilution; optionality in quantum networking/sensing adds upside.

**Bear Case (toward $12 or below):**
- Commercialization timeline slips; revenue disappoints vs. the steep consensus ramp, and the premium multiple compresses violently.
- A competing modality (superconducting, neutral-atom, photonic) wins, eroding IonQ's relevance.
- Continued cash burn forces repeated equity raises, diluting per-share value; sentiment-driven 3.0+ beta amplifies drawdowns (52-week range $25.89–$84.64 already shows ~3× swings).

---

## 10. Verdict

**Recommendation: SELL (valuation-driven), price target range $12–$36, base case ~$23.** IonQ is a credible technology leader with a genuinely strong balance sheet, and I do not dispute that quantum computing could become a large industry. The problem is entirely one of price: at $72 the stock carries a ~$26.9B market cap on $187M of trailing revenue (133× EV/revenue), and a disciplined forward EV/Revenue framework — projecting revenue to ~$957M by 2030 and applying a still-generous 12× exit multiple discounted at a 21.3% WACC — yields ~$18/share. A probability-weighted blend across bear/base/bull/hyper-bull scenarios lands near **$23**, implying roughly **68% downside**. Only a tail outcome (>$2.5B revenue in 2030 at a premium multiple) supports today's price.

**Confidence is Low**, by design: this is a binary, narrative-driven situation where outcomes are dispersed and unpredictable, and a high-beta name can stay expensive — or run further — on momentum and sector enthusiasm well beyond what fundamentals justify. Short-sellers face significant squeeze and timing risk despite the favorable risk/reward on paper.

**Practical guidance:** Existing holders sitting on gains should consider trimming into strength; new capital should *not* be committed at these levels on a fundamental basis. **Catalysts to watch:** quarterly revenue vs. the steep consensus ramp, gross-margin and cash-burn trajectory, technical milestones (qubit count/fidelity, error correction), large enterprise/government contract wins, and any equity raise (dilution signal). A re-rating toward fair value would more constructively be revisited after a meaningful price reset (toward the $25–$35 zone) or after revenue demonstrably tracks well above the modeled path. **Time horizon: 12–24 months.**

---
*This analysis is for informational purposes only and does not constitute investment advice.*
---