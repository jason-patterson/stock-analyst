#!/usr/bin/env python3
"""
Market Sentiment Agent
Reads tickers.txt, searches Reddit, StockTwits, financial news, and social media
for market sentiment on each ticker, then saves a report to reports/<TICKER>_sentiment.md
"""

import anthropic
import json
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────── Tools ───────────────────────────────────────────

TOOLS = [
    {
        "type": "web_search_20260209",
        "name": "web_search",
    },
    {
        "name": "save_report",
        "description": "Save the completed sentiment report as a markdown file in the reports/ directory.",
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

# ─────────────────────────── Save Report ─────────────────────────────────────

def save_sentiment_report(ticker: str, content: str) -> dict:
    path = Path("reports")
    path.mkdir(exist_ok=True)
    fp = path / f"{ticker}_sentiment.md"
    fp.write_text(content, encoding="utf-8")
    return {"saved": str(fp), "bytes": len(content.encode())}

# ─────────────────────────── System Prompt ───────────────────────────────────

SYSTEM = f"""You are a market sentiment analyst. Today's date is {datetime.now().strftime('%B %d, %Y')}.

Your job is to research current retail and institutional market sentiment for a given stock ticker
by searching the web. You have access to web_search — use it extensively.

══════════════════════════════════════════════════════════════
SEARCH STRATEGY — run ALL of these searches
══════════════════════════════════════════════════════════════
For ticker $TICKER, run searches covering:

1. Reddit sentiment:
   • "$TICKER site:reddit.com/r/wallstreetbets"
   • "$TICKER site:reddit.com/r/stocks"
   • "$TICKER site:reddit.com/r/investing"
   • "$TICKER site:reddit.com/r/SecurityAnalysis"

2. StockTwits & social:
   • "$TICKER site:stocktwits.com"
   • "$TICKER stock sentiment twitter"

3. Recent news sentiment:
   • "$TICKER stock analyst upgrade downgrade {datetime.now().strftime('%Y')}"
   • "$TICKER earnings outlook {datetime.now().strftime('%Y')}"
   • "$TICKER stock news {datetime.now().strftime('%B %Y')}"

4. Options / short interest:
   • "$TICKER short interest float"
   • "$TICKER options flow unusual activity"

5. Institutional:
   • "$TICKER institutional buying selling {datetime.now().strftime('%Y')}"
   • "$TICKER insider buying selling"

Run at least 8–10 searches total. Extract and synthesise findings across all sources.

══════════════════════════════════════════════════════════════
OUTPUT FORMAT
══════════════════════════════════════════════════════════════
After completing all searches, write a comprehensive markdown sentiment report with
this exact structure and save it using the save_report tool:

---
# [Company Name] ([TICKER]) — Market Sentiment Report

**Date:** [today] | **Analyst:** AI Sentiment Model

---

## Overall Sentiment Score

| Dimension | Score | Signal |
|-----------|-------|--------|
| Overall Sentiment | Bullish / Neutral / Bearish | 🟢 / 🟡 / 🔴 |
| Reddit / Retail | Bullish / Neutral / Bearish | |
| News & Media | Bullish / Neutral / Bearish | |
| Institutional | Bullish / Neutral / Bearish | |
| Options Flow | Bullish / Neutral / Bearish | |

**Sentiment Summary:** [2–3 sentence synthesis of overall market mood]

---

## Reddit & Social Media Sentiment

### r/WallStreetBets
[What WSB is saying — key posts, memes, DD threads, upvotes, general tone]

### r/stocks / r/investing
[More measured retail investor opinion — key themes, DD, concerns]

### StockTwits
[Short-form social sentiment — bull/bear ratio if found, top posts]

### Twitter / X
[Notable tweets, trending topics, influencer opinions if found]

---

## News & Media Sentiment

### Recent Headlines
[Bullet list of 5–10 recent headlines with sentiment label (Positive/Negative/Neutral)]

### Analyst Activity
[Recent upgrades, downgrades, price target changes, new coverage]

### Earnings & Guidance Sentiment
[Recent earnings reaction, guidance sentiment, beat/miss history]

---

## Institutional Sentiment

### Institutional Flows
[Recent 13F filings, notable buys/sells, hedge fund activity]

### Insider Activity
[Recent insider buys/sells — names, amounts, dates if found]

---

## Options & Short Interest

| Metric | Value | Signal |
|--------|-------|--------|
| Short Interest | X.X% of float | Bearish / Neutral |
| Short Squeeze Potential | High / Medium / Low | |
| Put/Call Ratio | X.XX | Bearish / Neutral / Bullish |
| Unusual Options Activity | Yes / No | |

[Commentary on options flow and what it implies]

---

## Bull Case (from the crowd)
[Top 3–5 bullish arguments being made on social media and news]

- **[Theme]:** [Detail]
- ...

## Bear Case (from the crowd)
[Top 3–5 bearish arguments, concerns, or risks being discussed]

- **[Theme]:** [Detail]
- ...

---

## Key Catalysts Being Watched

[List of upcoming events, earnings dates, product launches, regulatory decisions,
macro factors, etc. that are driving sentiment]

---

## Sentiment vs. Fundamentals

[Brief paragraph: does the crowd sentiment align or diverge from fundamental valuation?
Is this a sentiment-driven trade or fundamentally supported?]

---

## Sources Consulted
[Brief list of subreddits, sites, and search queries used]

---
*Sentiment analysis based on publicly available social media and news sources.
Not investment advice.*
---

Be thorough and specific — quote actual posts, headlines, or comments where possible.
If a search returns no relevant results, note it and move on.
"""

# ─────────────────────────── Agent Loop ──────────────────────────────────────

def analyze_sentiment(client: anthropic.Anthropic, ticker: str) -> None:
    print(f"\n{'─' * 62}")
    print(f"  Sentiment scan: {ticker}")
    print(f"{'─' * 62}")

    messages: list[dict] = [
        {
            "role": "user",
            "content": (
                f"Research and analyse the current market sentiment for ticker: **{ticker}**. "
                "Run all the searches described in your instructions, then write and save "
                "a complete sentiment report."
            ),
        }
    ]

    container_id: str | None = None

    for iteration in range(40):
        kwargs: dict = dict(
            model="claude-opus-4-8",
            max_tokens=16000,
            thinking={"type": "adaptive"},
            system=SYSTEM,
            tools=TOOLS,  # type: ignore[arg-type]
            messages=messages,
        )
        if container_id:
            kwargs["container"] = container_id

        response = client.messages.create(**kwargs)

        # Persist container across turns (required by web_search dynamic filtering)
        if hasattr(response, "container") and response.container:
            container_id = response.container.id

        # Collect assistant turn
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            print(f"  ✓ Sentiment report complete — {ticker}")
            break

        if response.stop_reason == "pause_turn":
            # Server-side web search hit its iteration limit — re-send to continue.
            # Do NOT add a new user message; the API resumes from the trailing server_tool_use block.
            continue

        if response.stop_reason != "tool_use":
            print(f"  Stopped: {response.stop_reason}")
            break

        # Handle custom tool calls (save_report).
        # web_search is server-side — its results are already embedded in response.content.
        tool_results = []
        for block in response.content:
            if block.type == "server_tool_use":
                query = block.input.get("query", "")
                print(f"  → web_search({query[:70]})")

            elif block.type == "tool_use":
                # Custom tool — only save_report for now
                if block.name == "save_report":
                    result = save_sentiment_report(
                        block.input["ticker"], block.input["content"]
                    )
                    print(f"  ✓ Saved → reports/{block.input['ticker']}_sentiment.md")
                else:
                    result = {"error": f"Unknown tool: {block.name}"}

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result, default=str),
                })

        if tool_results:
            messages.append({"role": "user", "content": tool_results})

    else:
        print(f"  Warning: max iterations reached for {ticker}")


# ─────────────────────────── Entry Point ─────────────────────────────────────

def main() -> None:
    tickers_file = Path("tickers.txt")
    if not tickers_file.exists():
        print("ERROR: tickers.txt not found.")
        sys.exit(1)

    tickers: list[str] = []
    for line in tickers_file.read_text().splitlines():
        parts = line.strip().split()
        if not parts:
            continue
        tok = parts[1] if len(parts) >= 2 and parts[0].isdigit() else parts[0]
        tickers.append(tok)

    print("═" * 62)
    print("  Market Sentiment Agent")
    print(f"  Date   : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Model  : claude-opus-4-8  (web search enabled)")
    print(f"  Tickers: {', '.join(tickers)}")
    print(f"  Output : reports/<TICKER>_sentiment.md")
    print("═" * 62)

    client = anthropic.Anthropic()

    for ticker in tickers:
        try:
            analyze_sentiment(client, ticker)
        except Exception as exc:
            print(f"  ERROR on {ticker}: {exc}")

    print("\n" + "═" * 62)
    print(f"  Done!  Reports in: {Path('reports').absolute()}")
    print("═" * 62)


if __name__ == "__main__":
    main()
