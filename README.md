# Stock Analyst Agent

An AI-powered stock analysis tool that performs institutional-grade **intrinsic value analysis** (DCF/WACC) and **market sentiment research** for any list of tickers.

## Features

### `main.py` — Fundamental Valuation Agent
- Fetches live financial data via Yahoo Finance
- Calculates **WACC** using CAPM (risk-free rate, beta, equity risk premium)
- Runs a **two-stage DCF model** with phase 1/2 growth and Gordon Growth terminal value
- Generates a **sensitivity analysis** table (WACC × growth rate grid)
- Handles special cases: ETFs (earnings yield approach), financials (P/E, P/Book, DDM), negative FCF (normalised)
- Saves a full markdown report to `reports/<TICKER>.md`

### `sentiment.py` — Market Sentiment Agent
- Searches Reddit (r/WallStreetBets, r/stocks, r/investing), StockTwits, Twitter/X, and financial news
- Analyses analyst upgrades/downgrades, insider activity, institutional flows
- Reviews short interest, put/call ratio, and unusual options activity
- Identifies bull/bear themes from the crowd
- Saves a markdown report to `reports/<TICKER>_sentiment.md`

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/jason-patterson/stock-analyst.git
cd stock-analyst
```

### 2. Create and activate a virtual environment
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. Add your Anthropic API key
Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=sk-ant-...
```
Get your key at [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys).

### 5. Edit your tickers
Open `tickers.txt` and add one ticker per line (with an optional line number prefix):
```
1	AAPL
2	MSFT
3	NVDA
```

## Usage

### Run the valuation agent
```powershell
python main.py
```

### Run the sentiment agent
```powershell
python sentiment.py
```

Reports are saved to the `reports/` directory.

## Output

| File | Description |
|------|-------------|
| `reports/<TICKER>.md` | Full DCF/WACC valuation report |
| `reports/<TICKER>_sentiment.md` | Market sentiment report |

### Valuation report includes
- Executive summary (intrinsic value vs market price, upside/downside %)
- Company overview and financial snapshot
- Full WACC derivation table
- 10-year DCF projection with valuation bridge
- Sensitivity analysis grid
- Relative valuation multiples
- Analyst consensus
- Bull/bear risks and investment verdict

### Sentiment report includes
- Overall sentiment score (Bullish / Neutral / Bearish)
- Reddit and social media analysis
- Recent news headlines with sentiment labels
- Analyst upgrades/downgrades
- Institutional and insider activity
- Short interest and options flow
- Key catalysts being watched

## Tech Stack

| Library | Purpose |
|---------|---------|
| `anthropic` | Claude Opus 4.8 — agent orchestration, web search |
| `yfinance` | Financial data (price, statements, ratios) |
| `pandas` | Data processing |
| `python-dotenv` | Environment variable management |

## Disclaimer

This tool is for informational and educational purposes only. Nothing in the output constitutes investment advice. Always do your own research before making investment decisions.
