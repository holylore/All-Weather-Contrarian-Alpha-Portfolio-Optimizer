# ── CELL 2 — MODEL CONFIGURATION ────────────────────────────
# This cell is the control center of the entire notebook.
# Every parameter reflects a deliberate choice from the
# investment model. To update the model, edit this cell only.
 
# -- Portfolio structure ---------------------------------------
TARGET_CORE       = 0.50   # 50% ETF Core
TARGET_SATELLITE  = 0.40   # 40% Equity Satellite
TARGET_LIQUIDITY  = 0.10   # 10% Cash reserve
 
# -- Equity positions (internal code → Yahoo Finance ticker) --
TICKER_MAP = {
    # Tech Pillar
    "NVDA": "NVDA",     # NVIDIA               (NASDAQ)
    "AMZN": "AMZN",     # Amazon               (NASDAQ)
    "MSFT": "MSFT",     # Microsoft            (NASDAQ)
    "PANW": "PANW",     # Palo Alto Networks   (NASDAQ)
    # Financial Pillar
    "SPGI": "SPGI",     # S&P Global           (NYSE)
    "V":    "V",        # Visa                 (NYSE)
    "JPM":  "JPM",      # JPMorgan Chase       (NYSE)
    # Defensive Pillar
    "PG":   "PG",       # Procter & Gamble     (NYSE)
    # Energy Pillar
    "VST":  "VST",      # Vistra Energy        (NYSE)
    # Sergeants
    "SPOT": "SPOT",     # Spotify              (NYSE)
    "AVGO": "AVGO",     # Broadcom             (NASDAQ)
    "WKL":  "WKL.AS",  # Wolters Kluwer       (Amsterdam)
    # Soldiers
    "CRM":  "CRM",      # Salesforce           (NYSE)
    "AMP":  "AMP.MI",  # Amplifon             (Milan)
}
 
# -- Satellite hierarchy (Pillar / Sergeant / Soldier) --------
HIERARCHY = {
    "Tech Pillar":       ["NVDA", "AMZN", "MSFT", "PANW"],
    "Financial Pillar":  ["SPGI", "V", "JPM"],
    "Defensive Pillar":  ["PG"],
    "Energy Pillar":     ["VST"],
    "Sergeants":         ["SPOT", "AVGO", "WKL"],
    "Soldiers":          ["CRM", "AMP"],
}
 
# -- Core ETF (ticker, target allocation, maximum cap) --------
ETF_MAP = {
    "BONDS": {
        "ticker": "IEAC.L",
        "target": 0.15,
        "max":    0.15,
        "name":   "iShares EUR Corp Bond",
    },
    "WORLD": {
        "ticker": "XDWD.DE",          # Proxy for Scalable MSCI World
        "target": 0.10,
        "max":    0.15,
        "name":   "Scalable MSCI World (proxy)",
    },
    "GOLD": {
        "ticker": "IGLN.L",
        "target": 0.075,
        "max":    0.125,
        "name":   "iShares Physical Gold",
    },
    "APAC": {
        "ticker": "HSXD.L",
        "target": 0.10,
        "max":    0.125,
        "name":   "HSBC Asia Pacific ex Japan",
    },
    "INDIA": {
        "ticker": "FLXI.L",
        "target": 0.05,
        "max":    0.075,
        "name":   "Franklin FTSE India",
    },
}
 
# -- Benchmark indices ----------------------------------------
BENCHMARK_MAP = {
    "EXW1": "EXW1.DE",   # iShares Core Euro Stoxx 50
    "IWDA": "IWDA.L",    # iShares Core MSCI World
    "VUSA": "VUSA.L",    # Vanguard S&P 500
}
 
# -- Global parameters ----------------------------------------
RISK_FREE_RATE = 0.03    # 3% annual (ECB reference rate)
TRADING_DAYS   = 252     # Standard trading days per year
START_DATE     = "2025-01-01"
 
# -- Optimizer constraints ------------------------------------
# Each stock is capped at 10% of total portfolio.
# Since Satellite = 40% of total, the cap within the bucket is:
# 10% / 40% = 25%
MAX_WEIGHT_SATELLITE = 0.10 / TARGET_SATELLITE   # 25% of bucket
MIN_WEIGHT_SATELLITE = 0.01                       # 1% minimum
 
# -- Current weights (from latest portfolio snapshot) ---------
# These are the actual allocation percentages as of April 2026,
# normalized to the Satellite bucket only.
CURRENT_WEIGHTS_RAW = {
    "NVDA": 0.1257, "AMZN": 0.0795, "MSFT": 0.0672,
    "PANW": 0.0524, "SPGI": 0.0692, "V":    0.0991,
    "JPM":  0.0491, "PG":   0.0690, "VST":  0.0761,
    "SPOT": 0.0822, "AVGO": 0.0630, "WKL":  0.0528,
    "CRM":  0.0866, "AMP":  0.0280,
}
total_satellite = sum(CURRENT_WEIGHTS_RAW.values())
CURRENT_WEIGHTS = {k: v / total_satellite
                   for k, v in CURRENT_WEIGHTS_RAW.items()}
 
print("✓ Configuration loaded.")
print(f"  Satellite positions : {len(TICKER_MAP)}")
print(f"  Core ETFs           : {len(ETF_MAP)}")
print(f"  Max weight per stock: {MAX_WEIGHT_SATELLITE:.0%} of bucket "
      f"(= 10% of total portfolio)")
