# Portfolio Optimizer — All-Weather + Contrarian Alpha

A Python-based quantitative analysis tool built on top of a personal
Core-Satellite investment model. Downloads historical price data via
`yfinance`, computes portfolio metrics, and runs a Markowitz mean-variance
optimizer separately on the equity Satellite and the ETF Core.

> **Backtest disclosure** — The portfolio reached its current composition
> in April 2026. All metrics and performance figures shown here are
> backtest results over the January 2025 – present window, not a live
> track record. The analysis is forward-looking: it informs future
> allocation decisions, not past performance claims.

---

## Model structure

The investment model — *All-Weather + Contrarian Alpha* — rethinks the
classic Core-Satellite framework:

| Bucket | Weight | Logic |
|---|---|---|
| **Core** | 50% | 5 ETFs. Dalio-inspired All-Weather diversification. Capital protection across market regimes. |
| **Satellite** | 40% | 14 equities. Graham margin of safety + Munger MOAT quality. Alpha generation. |
| **Liquidity** | 10% | Cash reserve. Never deployed under pressure. |

The Satellite has an internal hierarchy:

- **Pillars** — wide MOAT businesses, maximum conviction, held long-term
- **Sergeants** — high-quality candidates proving themselves over consecutive quarters
- **Soldiers** — positions under evaluation

Each equity position has a **Kill Switch**: one fundamental criterion
(e.g. Azure Revenue Growth YoY, CET1 Ratio, ARR Renewal Rate) that
triggers a review if breached — regardless of market price.

---

## Repository structure

```
portfolio-optimizer/
│
├── portfolio_manager_EN.py   # Full analysis — 6 logical cells
└── README.md
```

The code is organized in six sequential sections, designed to run
top-to-bottom in a Jupyter / Google Colab notebook:

| Cell | Name | Description |
|---|---|---|
| 1 | Environment setup | Library installation and imports |
| 2 | Model configuration | Ticker map, hierarchy, ETF targets, optimizer constraints |
| 3 | Data download | Single `yfinance` call for all 22 instruments + download report |
| 4 | Portfolio metrics | Annualized return, volatility, Sharpe ratio, max drawdown |
| 5 | Markowitz optimization | Max-Sharpe optimizer on Satellite and Core separately |
| 6 | Visualization | 5 charts: scatter, Sharpe ranking, weight comparison, cumulative performance |

---

## How to run

**Option A — Google Colab (recommended)**

1. Open [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy each cell section from `portfolio_manager_EN.py` in order
4. Run with `Shift + Enter`, one cell at a time

**Option B — Local Jupyter**

```bash
pip install yfinance scipy matplotlib seaborn pandas numpy
jupyter notebook
```

Remove the `!pip install` line from Cell 1 before running.

---

## Key results (backtest period: Jan 2025 – May 2026)

| Component | Sharpe Ratio | vs IWDA benchmark (1.28) |
|---|---|---|
| Core ETF (optimal) | 1.78 | +0.5 |
| Satellite (optimal) | 0.92 | −0.36 |
| Satellite (current weights) | see chart | — |

The Core outperforms all three benchmark indices on a risk-adjusted basis.
The Satellite underperforms IWDA in this period — a result consistent with
broader underperformance of European compounders and SaaS names in 2025.
The optimizer concentrates the Satellite on NVDA, AVGO, JPM, and PANW;
it reduces or minimizes exposure to positions with negative Sharpe in the window.

Scheduled fundamental review: **every quarter**.

---

## Technical notes

**Universe**
- 14 equity positions (NYSE / NASDAQ / Amsterdam / Milan)
- 5 Core ETFs (London Stock Exchange / Xetra)
- 3 benchmark indices: EXW1, IWDA, VUSA
- Source: Yahoo Finance via `yfinance` (adjusted close prices)

**Optimizer**
- Algorithm: Sequential Least Squares Programming (`scipy.optimize.minimize`, method `SLSQP`)
- Objective: maximize Sharpe ratio (minimizes negative Sharpe)
- Satellite constraints: each position between 1% and 25% of bucket
  (equivalent to 0.4% – 10% of total portfolio)
- Core constraints: each ETF between 0% and its model-defined maximum

<img width="966" height="1036" alt="image" src="https://github.com/user-attachments/assets/ec89c50c-892c-4fd8-8a43-40e51da5d793" />

**Limitations**
- 16-month backtest window is not statistically sufficient for strategy validation
- Markowitz assumes normally distributed returns — an approximation
- The Scalable MSCI World ETF (LU2903252349) is approximated by `XDWD.DE`
  as a structural proxy (same underlying index, different fund)
- Kill Switch fundamental data is updated manually after each earnings season;
  it is not fetched automatically from Yahoo Finance

---

## Development process

This project was built through **vibe coding**: an AI-assisted workflow
where the investment logic, model structure, and analytical decisions
were defined by the author, and Claude (Anthropic) was used to translate
them into working Python code.

The author has a self-taught Python background (~77 days of daily practice,
no formal CS education) and no prior experience with quantitative finance
libraries. Every parameter, constraint, hierarchy, and interpretation in
this codebase reflects the author's own investment reasoning.

Code style follows PEP 8 conventions. Variables and comments are in English
for international readability. The narrative version of this analysis —
with methodology explanation and investment thesis — is published as a
Kaggle notebook (link below).

---

## Links

- **Kaggle notebook** — narrative version with methodology and conclusions: [https://www.kaggle.com/code/lorenzopardini/all-weather-contrarian-alpha-portfolio-optimizer/edit]
- **Personal site** — full investment method, Tableau dashboard, project portfolio: [https://lorenzopardini.lovable.app]

---

## Disclaimer

This project is a personal learning exercise combining quantitative finance,
Python development, and long-term investment discipline.
It is not financial advice. Past backtest results do not guarantee future performance.
