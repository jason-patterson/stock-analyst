#!/usr/bin/env python3
"""
Stock Analyst Agent
Reads tickers.txt, performs DCF/WACC intrinsic value analysis for each ticker,
and saves a comprehensive markdown report to reports/<TICKER>.md
"""

import anthropic
import yfinance as yf
import json
import sys
from pathlib import Path
import pandas as pd
from datetime import datetime

# ─────────────────────────── Helpers ─────────────────────────────────────────

def _f(value) -> float | None:
    """Safe float conversion."""
    try:
        if value is None:
            return None
        v = float(value)
        return None if (v != v) else v  # NaN check
    except (TypeError, ValueError):
        return None


def _fmt_b(v) -> str:
    """Format a dollar value in billions."""
    if v is None:
        return "N/A"
    b = v / 1e9
    return f"${b:.2f}B"


# ─────────────────────────── Tool Implementations ────────────────────────────

def get_stock_data(ticker: str) -> dict:
    """Fetch current price, market data, valuation multiples, and company overview."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "ticker": ticker,
            "company_name": info.get("longName", ticker),
            "quote_type": info.get("quoteType"),          # "ETF", "EQUITY", etc.
            "current_price": _f(info.get("currentPrice") or info.get("regularMarketPrice")),
            "previous_close": _f(info.get("previousClose")),
            "52w_high": _f(info.get("fiftyTwoWeekHigh")),
            "52w_low": _f(info.get("fiftyTwoWeekLow")),
            "market_cap": _f(info.get("marketCap")),
            "enterprise_value": _f(info.get("enterpriseValue")),
            "shares_outstanding": _f(info.get("sharesOutstanding")),
            "float_shares": _f(info.get("floatShares")),
            "beta": _f(info.get("beta")),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "country": info.get("country"),
            # Balance sheet snapshot
            "total_debt": _f(info.get("totalDebt")),
            "total_cash": _f(info.get("totalCash")),
            # Cash flows
            "free_cash_flow_ttm": _f(info.get("freeCashflow")),
            "operating_cash_flow_ttm": _f(info.get("operatingCashflow")),
            # Income
            "revenue_ttm": _f(info.get("totalRevenue")),
            "ebitda_ttm": _f(info.get("ebitda")),
            "net_income_ttm": _f(info.get("netIncomeToCommon")),
            "eps_ttm": _f(info.get("trailingEps")),
            "eps_forward": _f(info.get("forwardEps")),
            # Multiples
            "pe_ttm": _f(info.get("trailingPE")),
            "pe_forward": _f(info.get("forwardPE")),
            "ev_ebitda": _f(info.get("enterpriseToEbitda")),
            "ev_revenue": _f(info.get("enterpriseToRevenue")),
            "price_to_book": _f(info.get("priceToBook")),
            "price_to_sales": _f(info.get("priceToSalesTrailing12Months")),
            "peg_ratio": _f(info.get("pegRatio")),
            # Growth & profitability
            "revenue_growth_yoy": _f(info.get("revenueGrowth")),
            "earnings_growth_yoy": _f(info.get("earningsGrowth")),
            "profit_margin": _f(info.get("profitMargins")),
            "operating_margin": _f(info.get("operatingMargins")),
            "return_on_equity": _f(info.get("returnOnEquity")),
            "return_on_assets": _f(info.get("returnOnAssets")),
            "debt_to_equity": _f(info.get("debtToEquity")),
            # Cost of debt estimation
            "interest_expense": _f(info.get("interestExpense")),
            "effective_tax_rate": _f(info.get("effectiveTaxRate")),
            # Analyst consensus
            "analyst_target_mean": _f(info.get("targetMeanPrice")),
            "analyst_target_high": _f(info.get("targetHighPrice")),
            "analyst_target_low": _f(info.get("targetLowPrice")),
            "analyst_count": info.get("numberOfAnalystOpinions"),
            "recommendation_key": info.get("recommendationKey"),
            "recommendation_mean": _f(info.get("recommendationMean")),
            # Dividend
            "dividend_yield": _f(info.get("dividendYield")),
            "payout_ratio": _f(info.get("payoutRatio")),
            # Business description (truncated)
            "description": (info.get("longBusinessSummary") or "")[:700],
        }
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}


def get_financial_statements(ticker: str) -> dict:
    """Fetch 4 years of income statement, balance sheet, and cash flow history."""
    try:
        stock = yf.Ticker(ticker)
        result: dict = {
            "fcf_history": {},
            "revenue_history": {},
            "net_income_history": {},
            "ebit_history": {},
            "operating_cf_history": {},
            "capex_history": {},
            "total_debt_history": {},
            "cash_history": {},
        }

        # ── Cash Flow ──────────────────────────────────────────────
        cf = stock.cashflow
        if cf is not None and not cf.empty:
            OCF_KEYS = ["Operating Cash Flow", "Cash From Operating Activities",
                        "Total Cash From Operating Activities"]
            CAP_KEYS = ["Capital Expenditure", "Purchase Of Property Plant And Equipment",
                        "Capital Expenditures"]

            for col in cf.columns[:4]:
                yr = str(col.year)
                for k in OCF_KEYS:
                    if k in cf.index:
                        v = _f(cf.loc[k, col])
                        if v is not None:
                            result["operating_cf_history"][yr] = v
                            break
                for k in CAP_KEYS:
                    if k in cf.index:
                        v = _f(cf.loc[k, col])
                        if v is not None:
                            result["capex_history"][yr] = v
                            break
                ocf = result["operating_cf_history"].get(yr)
                cap = result["capex_history"].get(yr)
                if ocf is not None and cap is not None:
                    result["fcf_history"][yr] = ocf + cap  # capex is negative
                elif ocf is not None:
                    result["fcf_history"][yr] = ocf

        # ── Income Statement ───────────────────────────────────────
        inc = stock.financials
        if inc is not None and not inc.empty:
            REV_KEYS = ["Total Revenue", "Revenue"]
            NI_KEYS  = ["Net Income", "Net Income Common Stockholders",
                        "Net Income From Continuing Operations"]
            EBIT_KEYS = ["EBIT", "Operating Income"]

            for col in inc.columns[:4]:
                yr = str(col.year)
                for k in REV_KEYS:
                    if k in inc.index:
                        v = _f(inc.loc[k, col])
                        if v is not None:
                            result["revenue_history"][yr] = v; break
                for k in NI_KEYS:
                    if k in inc.index:
                        v = _f(inc.loc[k, col])
                        if v is not None:
                            result["net_income_history"][yr] = v; break
                for k in EBIT_KEYS:
                    if k in inc.index:
                        v = _f(inc.loc[k, col])
                        if v is not None:
                            result["ebit_history"][yr] = v; break

        # ── Balance Sheet ──────────────────────────────────────────
        bs = stock.balance_sheet
        if bs is not None and not bs.empty:
            DEBT_KEYS = ["Total Debt", "Long Term Debt",
                         "Long Term Debt And Capital Lease Obligation"]
            CASH_KEYS = ["Cash And Cash Equivalents",
                         "Cash Cash Equivalents And Short Term Investments"]

            for col in bs.columns[:4]:
                yr = str(col.year)
                for k in DEBT_KEYS:
                    if k in bs.index:
                        v = _f(bs.loc[k, col])
                        if v is not None:
                            result["total_debt_history"][yr] = v; break
                for k in CASH_KEYS:
                    if k in bs.index:
                        v = _f(bs.loc[k, col])
                        if v is not None:
                            result["cash_history"][yr] = v; break

        return result
    except Exception as e:
        return {"error": str(e)}


def get_analyst_estimates(ticker: str) -> dict:
    """Fetch analyst price targets, recommendations, EPS estimates, and growth rates."""
    try:
        stock = yf.Ticker(ticker)
        info  = stock.info
        result: dict = {
            "analyst_mean_target":   _f(info.get("targetMeanPrice")),
            "analyst_high_target":   _f(info.get("targetHighPrice")),
            "analyst_low_target":    _f(info.get("targetLowPrice")),
            "analyst_count":         info.get("numberOfAnalystOpinions"),
            "recommendation_key":    info.get("recommendationKey"),
            "recommendation_mean":   _f(info.get("recommendationMean")),
            "peg_ratio":             _f(info.get("pegRatio")),
            "earnings_qtly_growth":  _f(info.get("earningsQuarterlyGrowth")),
            "revenue_growth_yoy":    _f(info.get("revenueGrowth")),
        }
        for attr in ("earnings_estimate", "revenue_estimate", "eps_trend",
                     "growth_estimates"):
            try:
                data = getattr(stock, attr, None)
                if data is not None and not data.empty:
                    result[attr] = data.to_dict()
            except Exception:
                pass
        return result
    except Exception as e:
        return {"error": str(e)}


def calculate_wacc(
    beta: float,
    risk_free_rate: float,
    equity_risk_premium: float,
    cost_of_debt: float,
    tax_rate: float,
    market_cap: float,
    total_debt: float,
) -> dict:
    """
    WACC = (E/V × Ke) + (D/V × Kd × (1 − t))
    Ke = Rf + β × ERP  (CAPM)
    """
    total_debt = max(total_debt, 0.0)
    ke = risk_free_rate + beta * equity_risk_premium
    total_capital = market_cap + total_debt
    if total_capital <= 0:
        return {"error": "Total capital is zero or negative"}
    we = market_cap / total_capital
    wd = total_debt / total_capital
    kd_at = cost_of_debt * (1.0 - tax_rate)
    wacc  = we * ke + wd * kd_at
    return {
        "wacc":                   wacc,
        "wacc_pct":               round(wacc * 100, 2),
        "cost_of_equity_pct":     round(ke * 100, 2),
        "after_tax_cost_debt_pct": round(kd_at * 100, 2),
        "equity_weight_pct":      round(we * 100, 1),
        "debt_weight_pct":        round(wd * 100, 1),
        "inputs": {
            "beta":                    beta,
            "risk_free_rate_pct":      round(risk_free_rate * 100, 2),
            "equity_risk_premium_pct": round(equity_risk_premium * 100, 2),
            "pre_tax_cost_debt_pct":   round(cost_of_debt * 100, 2),
            "tax_rate_pct":            round(tax_rate * 100, 1),
            "market_cap_B":            round(market_cap / 1e9, 2),
            "total_debt_B":            round(total_debt / 1e9, 2),
        },
    }


def run_dcf(
    base_fcf: float,
    growth_rate_phase1: float,
    growth_rate_phase2: float,
    phase1_years: int,
    terminal_growth_rate: float,
    wacc: float,
    total_debt: float,
    cash_and_equivalents: float,
    shares_outstanding: float,
) -> dict:
    """
    Two-stage DCF model.
    Phase 1 (years 1–phase1_years): high-growth period.
    Phase 2 (remaining years to reach 10 total): lower growth.
    Terminal value via Gordon Growth Model.
    """
    total_debt = max(total_debt, 0.0)
    if wacc <= terminal_growth_rate:
        return {"error": f"WACC ({wacc:.2%}) must exceed terminal growth rate ({terminal_growth_rate:.2%})"}
    if shares_outstanding <= 0:
        return {"error": "Shares outstanding must be positive"}

    fcfs: list[float] = []
    pv_fcfs: list[float] = []
    current_fcf = base_fcf

    for i in range(10):
        g = growth_rate_phase1 if i < phase1_years else growth_rate_phase2
        current_fcf *= (1.0 + g)
        pv = current_fcf / ((1.0 + wacc) ** (i + 1))
        fcfs.append(current_fcf)
        pv_fcfs.append(pv)

    terminal_fcf = fcfs[-1] * (1.0 + terminal_growth_rate)
    terminal_value = terminal_fcf / (wacc - terminal_growth_rate)
    pv_tv = terminal_value / ((1.0 + wacc) ** 10)

    sum_pv = sum(pv_fcfs)
    ev = sum_pv + pv_tv
    equity_val = ev - total_debt + cash_and_equivalents
    intrinsic = equity_val / shares_outstanding

    return {
        "intrinsic_value_per_share":  round(intrinsic, 2),
        "enterprise_value_B":         round(ev / 1e9, 2),
        "equity_value_B":             round(equity_val / 1e9, 2),
        "sum_pv_fcfs_B":              round(sum_pv / 1e9, 2),
        "pv_terminal_value_B":        round(pv_tv / 1e9, 2),
        "terminal_value_B":           round(terminal_value / 1e9, 2),
        "tv_pct_of_ev":               round(pv_tv / ev * 100, 1) if ev else None,
        "projected_fcfs_M":           [round(f / 1e6, 0) for f in fcfs],
        "pv_fcfs_M":                  [round(f / 1e6, 0) for f in pv_fcfs],
        "inputs": {
            "base_fcf_M":             round(base_fcf / 1e6, 0),
            "growth_phase1_pct":      round(growth_rate_phase1 * 100, 1),
            "growth_phase2_pct":      round(growth_rate_phase2 * 100, 1),
            "phase1_years":           phase1_years,
            "terminal_growth_pct":    round(terminal_growth_rate * 100, 1),
            "wacc_pct":               round(wacc * 100, 2),
            "total_debt_B":           round(total_debt / 1e9, 2),
            "cash_B":                 round(cash_and_equivalents / 1e9, 2),
            "shares_M":               round(shares_outstanding / 1e6, 1),
        },
    }


def run_sensitivity(
    base_fcf: float,
    wacc_values: list,
    phase1_growth_values: list,
    phase1_years: int,
    phase2_growth: float,
    terminal_growth: float,
    total_debt: float,
    cash: float,
    shares: float,
) -> dict:
    """Grid of intrinsic values across WACC × Phase1-growth combinations."""
    grid: dict = {}
    for g in phase1_growth_values:
        row_key = f"{g*100:.0f}% growth"
        grid[row_key] = {}
        for w in wacc_values:
            col_key = f"{w*100:.1f}% WACC"
            if w <= terminal_growth:
                grid[row_key][col_key] = "N/A"
            else:
                r = run_dcf(
                    base_fcf=base_fcf,
                    growth_rate_phase1=g,
                    growth_rate_phase2=phase2_growth,
                    phase1_years=phase1_years,
                    terminal_growth_rate=terminal_growth,
                    wacc=w,
                    total_debt=total_debt,
                    cash_and_equivalents=cash,
                    shares_outstanding=shares,
                )
                v = r.get("intrinsic_value_per_share", "Err")
                grid[row_key][col_key] = f"${v:.2f}" if isinstance(v, float) else v
    return {"sensitivity_grid": grid,
            "rows": "Phase-1 FCF Growth Rate",
            "cols": "WACC"}


def save_report(ticker: str, content: str) -> dict:
    """Write the markdown report to reports/<TICKER>.md"""
    path = Path("reports")
    path.mkdir(exist_ok=True)
    fp = path / f"{ticker}.md"
    fp.write_text(content, encoding="utf-8")
    return {"saved": str(fp), "bytes": len(content.encode())}


# ─────────────────────────── Tool Definitions ─────────────────────────────────

TOOLS: list[dict] = [
    {
        "name": "get_stock_data",
        "description": (
            "Fetch current market data for a stock: price, market cap, beta, "
            "valuation multiples, profitability metrics, analyst targets, and company overview."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"ticker": {"type": "string"}},
            "required": ["ticker"],
        },
    },
    {
        "name": "get_financial_statements",
        "description": (
            "Fetch 4 years of historical financial statements: "
            "FCF, revenue, net income, EBIT, operating CF, capex, total debt, cash."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"ticker": {"type": "string"}},
            "required": ["ticker"],
        },
    },
    {
        "name": "get_analyst_estimates",
        "description": (
            "Fetch analyst consensus data: price targets, recommendation ratings, "
            "EPS estimates, and forward growth estimates."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"ticker": {"type": "string"}},
            "required": ["ticker"],
        },
    },
    {
        "name": "calculate_wacc",
        "description": (
            "Calculate the Weighted Average Cost of Capital (WACC) using CAPM for cost of equity. "
            "Ke = Rf + β × ERP.  WACC = (E/V × Ke) + (D/V × Kd × (1−t))."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "beta":                 {"type": "number", "description": "Stock beta"},
                "risk_free_rate":       {"type": "number", "description": "Risk-free rate as decimal (e.g. 0.045)"},
                "equity_risk_premium":  {"type": "number", "description": "ERP as decimal (typically 0.055)"},
                "cost_of_debt":         {"type": "number", "description": "Pre-tax cost of debt as decimal"},
                "tax_rate":             {"type": "number", "description": "Corporate tax rate as decimal"},
                "market_cap":           {"type": "number", "description": "Market cap in dollars"},
                "total_debt":           {"type": "number", "description": "Total debt in dollars"},
            },
            "required": ["beta", "risk_free_rate", "equity_risk_premium",
                         "cost_of_debt", "tax_rate", "market_cap", "total_debt"],
        },
    },
    {
        "name": "run_dcf",
        "description": (
            "Two-stage DCF model: project FCFs for 10 years (phase1=high growth, phase2=lower growth), "
            "compute Gordon Growth terminal value, derive intrinsic equity value per share."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "base_fcf":             {"type": "number", "description": "TTM free cash flow in dollars"},
                "growth_rate_phase1":   {"type": "number", "description": "Phase-1 annual FCF growth rate as decimal"},
                "growth_rate_phase2":   {"type": "number", "description": "Phase-2 annual FCF growth rate as decimal"},
                "phase1_years":         {"type": "integer", "description": "Duration of Phase 1 (1–8)"},
                "terminal_growth_rate": {"type": "number", "description": "Perpetual terminal growth rate as decimal"},
                "wacc":                 {"type": "number", "description": "WACC as decimal"},
                "total_debt":           {"type": "number", "description": "Total debt in dollars"},
                "cash_and_equivalents": {"type": "number", "description": "Cash in dollars"},
                "shares_outstanding":   {"type": "number", "description": "Total shares"},
            },
            "required": ["base_fcf", "growth_rate_phase1", "growth_rate_phase2",
                         "phase1_years", "terminal_growth_rate", "wacc",
                         "total_debt", "cash_and_equivalents", "shares_outstanding"],
        },
    },
    {
        "name": "run_sensitivity",
        "description": (
            "Run DCF across a grid of WACC values × Phase-1 growth rates to produce "
            "a sensitivity table of intrinsic values per share."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "base_fcf":             {"type": "number"},
                "wacc_values":          {"type": "array", "items": {"type": "number"},
                                         "description": "List of WACC decimals to test (e.g. [0.07,0.08,0.09,0.10,0.11])"},
                "phase1_growth_values": {"type": "array", "items": {"type": "number"},
                                         "description": "List of Phase-1 growth rates to test"},
                "phase1_years":         {"type": "integer"},
                "phase2_growth":        {"type": "number"},
                "terminal_growth":      {"type": "number"},
                "total_debt":           {"type": "number"},
                "cash":                 {"type": "number"},
                "shares":               {"type": "number"},
            },
            "required": ["base_fcf", "wacc_values", "phase1_growth_values",
                         "phase1_years", "phase2_growth", "terminal_growth",
                         "total_debt", "cash", "shares"],
        },
    },
    {
        "name": "save_report",
        "description": "Save the completed analysis as a markdown file in the reports/ directory.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker":  {"type": "string"},
                "content": {"type": "string", "description": "Full markdown report content"},
            },
            "required": ["ticker", "content"],
        },
    },
]

# ─────────────────────────── Tool Dispatch ────────────────────────────────────

DISPATCH = {
    "get_stock_data":        lambda i: get_stock_data(i["ticker"]),
    "get_financial_statements": lambda i: get_financial_statements(i["ticker"]),
    "get_analyst_estimates": lambda i: get_analyst_estimates(i["ticker"]),
    "calculate_wacc":        lambda i: calculate_wacc(**i),
    "run_dcf":               lambda i: run_dcf(**i),
    "run_sensitivity":       lambda i: run_sensitivity(**i),
    "save_report":           lambda i: save_report(i["ticker"], i["content"]),
}

# ─────────────────────────── System Prompt ───────────────────────────────────

SYSTEM = f"""You are a senior equity research analyst at a top-tier investment bank.
Today's date: {datetime.now().strftime('%B %d, %Y')}.

Your job is to produce a rigorous, institutional-grade intrinsic value analysis for each
stock ticker you receive. Follow these steps exactly:

══════════════════════════════════════════════════════════════
STEP 1 — DATA COLLECTION (always run all three)
══════════════════════════════════════════════════════════════
1. get_stock_data(ticker)
2. get_financial_statements(ticker)
3. get_analyst_estimates(ticker)

══════════════════════════════════════════════════════════════
STEP 2 — SPECIAL-CASE SCREENING
══════════════════════════════════════════════════════════════
• ETFs (e.g. SPY, QQQ): FCF-based DCF doesn't apply directly. Instead, analyse
  the underlying index via earnings yield, trailing/forward P/E vs. historical norms,
  and expected return. Estimate a "fair value range" based on a normalised P/E.
• Financial companies (banks, asset managers, PE firms such as KKR, BX, DB):
  FCF is less meaningful. Use Price-to-Earnings, Price-to-Book, and/or Dividend
  Discount Model. Explain your approach clearly.
• If FCF is negative: use average of available years (normalised FCF), or note the
  limitation and apply an EV/Revenue or EV/EBITDA-based valuation instead.

══════════════════════════════════════════════════════════════
STEP 3 — WACC CALCULATION
══════════════════════════════════════════════════════════════
Call calculate_wacc with:
• risk_free_rate = 0.045  (10-year US Treasury approximation)
• equity_risk_premium = 0.055  (Damodaran consensus)
• cost_of_debt: derive from (interest_expense / total_debt).
  Fallback: 0.055 for investment-grade, 0.065 for high-yield or if data missing.
• tax_rate: use effective_tax_rate from data; fallback to 0.21 if unavailable.
• beta: from stock data. If missing/unreliable (ETF, financial), use sector beta
  (Tech 1.2, Financials 1.1, Healthcare 0.8, Industrials 1.0, Utilities 0.6).

══════════════════════════════════════════════════════════════
STEP 4 — DCF ANALYSIS
══════════════════════════════════════════════════════════════
Call run_dcf with carefully justified assumptions:
• base_fcf: TTM FCF. If negative, normalise. Document your choice.
• growth_rate_phase1 (years 1–5): blend of historical FCF CAGR, analyst EPS growth,
  and business fundamentals. Cap at 50%.
• growth_rate_phase2 (years 6–10): typically 40–60% of phase-1 rate, declining.
• phase1_years: usually 5.
• terminal_growth_rate: 2.5% for healthy US growers; 2.0% for mature/slow-growth.
• wacc: from Step 3.

Then call run_sensitivity with:
• wacc_values: WACC ± 2–4 percentage points (5 values)
• phase1_growth_values: base ± 5–10 ppt (5 values)

══════════════════════════════════════════════════════════════
STEP 5 — WRITE AND SAVE THE REPORT
══════════════════════════════════════════════════════════════
Call save_report with a complete professional markdown report following this structure:

---
# [Company Name] ([TICKER]) — Intrinsic Value Analysis

**Analysis Date:** [today] | **Analyst:** AI Research Model | **Price at Analysis:** $X.XX

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $X.XX |
| DCF Intrinsic Value | $X.XX |
| Upside / Downside | +/−X.X% |
| Analyst Consensus Target | $X.XX |
| Recommendation | BUY / HOLD / SELL |
| Confidence | High / Medium / Low |

**Thesis in one sentence:** [Your investment thesis]

---

## 2. Company Overview
[2–3 paragraphs: business model, revenue streams, competitive moat, key risks]

---

## 3. Financial Snapshot

| Metric | TTM Value |
|--------|-----------|
| Revenue | $X.XB |
| EBITDA | $X.XB |
| Free Cash Flow | $X.XB |
| Net Income | $X.XB |
| FCF Margin | X.X% |
| Revenue Growth YoY | X.X% |
| Return on Equity | X.X% |

[Brief commentary on trends, margins, and quality of earnings]

---

## 4. Valuation — WACC Derivation

| Input | Value | Source / Rationale |
|-------|-------|--------------------|
| Risk-Free Rate (Rf) | 4.50% | 10-yr US Treasury |
| Equity Risk Premium (ERP) | 5.50% | Damodaran |
| Beta (β) | X.XX | [Source] |
| Cost of Equity (Ke = Rf + β×ERP) | X.XX% | CAPM |
| Pre-tax Cost of Debt | X.XX% | [Calc or assumption] |
| Effective Tax Rate | X.X% | [Source] |
| After-tax Cost of Debt | X.XX% | |
| Equity Weight (E/V) | X.X% | Market cap / (Mkt cap + Debt) |
| Debt Weight (D/V) | X.X% | |
| **WACC** | **X.XX%** | |

---

## 5. DCF Model

### Assumptions
| Assumption | Value | Rationale |
|------------|-------|-----------|
| Base FCF | $X.XB | [TTM or normalised — explain] |
| Phase-1 Growth (yrs 1–X) | X.X% | [Historical CAGR, analyst ests.] |
| Phase-2 Growth (yrs X–10) | X.X% | [Justification] |
| Terminal Growth Rate | X.X% | [GDP proxy] |
| WACC | X.XX% | [From above] |

### 10-Year FCF Projection ($ millions)

| Year | Projected FCF | PV of FCF |
|------|--------------|-----------|
| 1 | $X | $X |
... (10 rows)

### Valuation Bridge
| Component | Value |
|-----------|-------|
| Sum of PV (FCFs) | $X.XB |
| PV of Terminal Value | $X.XB |
| Enterprise Value | $X.XB |
| (−) Total Debt | ($X.XB) |
| (+) Cash | $X.XB |
| Equity Value | $X.XB |
| Shares Outstanding | X.XB |
| **Intrinsic Value / Share** | **$X.XX** |
| Terminal Value % of EV | X.X% |

---

## 6. Sensitivity Analysis — Intrinsic Value per Share

[Paste the grid from run_sensitivity here as a markdown table]

---

## 7. Relative Valuation

| Multiple | Company | Sector Avg | Comment |
|----------|---------|------------|---------|
| P/E (TTM) | X.Xx | — | [Over/fairly/undervalued?] |
| Forward P/E | X.Xx | — | |
| EV/EBITDA | X.Xx | — | |
| P/S | X.Xx | — | |
| P/B | X.Xx | — | |

---

## 8. Analyst Consensus

| Metric | Value |
|--------|-------|
| Mean Price Target | $X.XX |
| High Target | $X.XX |
| Low Target | $X.XX |
| Number of Analysts | X |
| Recommendation | Buy / Hold / Sell |

---

## 9. Investment Risks

**Bull Case (+X% upside):** [3 bullet points]

**Bear Case (−X% downside):** [3 bullet points]

---

## 10. Verdict

[2–3 paragraph investment conclusion: BUY / HOLD / SELL with a clear price target range,
key catalysts to watch, and time horizon]

---
*This analysis is for informational purposes only and does not constitute investment advice.*
---

Always be explicit about your assumptions and their rationale. Show your work clearly.
If data is missing, state your substitute assumption and why."""


# ─────────────────────────── Agent Loop ──────────────────────────────────────

def analyze_ticker(client: anthropic.Anthropic, ticker: str) -> None:
    print(f"\n{'─' * 62}")
    print(f"  Analyzing: {ticker}")
    print(f"{'─' * 62}")

    messages: list[dict] = [
        {
            "role": "user",
            "content": (
                f"Perform a complete intrinsic value analysis for ticker: **{ticker}**. "
                "Follow all steps in your instructions precisely and save the final report."
            ),
        }
    ]

    for iteration in range(30):
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=16000,
            thinking={"type": "adaptive"},
            system=SYSTEM,
            tools=TOOLS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            print(f"  ✓ Analysis complete — {ticker}")
            break

        if response.stop_reason != "tool_use":
            print(f"  Stopped: {response.stop_reason}")
            break

        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue

            fn = DISPATCH.get(block.name)
            if fn is None:
                result: dict = {"error": f"Unknown tool: {block.name}"}
            else:
                try:
                    result = fn(block.input)
                except Exception as exc:
                    result = {"error": str(exc)}

            # Progress logging
            label = block.input.get("ticker", "")
            if block.name == "save_report":
                print(f"  ✓ Report saved → reports/{block.input.get('ticker','?')}.md")
            else:
                print(f"  → {block.name}({label})")

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": json.dumps(result, indent=2, default=str),
            })

        messages.append({"role": "user", "content": tool_results})
    else:
        print(f"  Warning: max iterations reached for {ticker}")


# ─────────────────────────── Entry Point ─────────────────────────────────────

def main() -> None:
    tickers_file = Path("tickers.txt")
    if not tickers_file.exists():
        print("ERROR: tickers.txt not found in the current directory.")
        sys.exit(1)

    tickers: list[str] = []
    for line in tickers_file.read_text().splitlines():
        parts = line.strip().split()
        if not parts:
            continue
        # Handle "1\tNOW" or just "NOW"
        tok = parts[1] if len(parts) >= 2 and parts[0].isdigit() else parts[0]
        tickers.append(tok)

    print("═" * 62)
    print("  Stock Analyst Agent")
    print(f"  Date   : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Model  : claude-opus-4-8  (adaptive thinking)")
    print(f"  Tickers: {', '.join(tickers)}")
    print(f"  Output : reports/<TICKER>.md")
    print("═" * 62)

    client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from env

    for ticker in tickers:
        try:
            analyze_ticker(client, ticker)
        except Exception as exc:
            print(f"  ERROR on {ticker}: {exc}")

    print("\n" + "═" * 62)
    print(f"  All done!  Reports saved in: {Path('reports').absolute()}")
    print("═" * 62)


if __name__ == "__main__":
    main()
