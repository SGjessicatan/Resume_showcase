"""Data loading and return calculation for the SGX risk engine.

Uses public price data only (Yahoo Finance via yfinance). Prices are cached
locally in data/ so the notebooks run offline after the first download.
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

# Yahoo Finance tickers for SGX-listed names (verify each one loads before relying on it)
TICKERS = {
    "DBS": "D05.SI",
    "OCBC": "O39.SI",
    "UOB": "U11.SI",
    "STI_ETF": "ES3.SI",
    "CICT": "C38U.SI",
}


def download_prices(start="2015-01-01", end=None, cache=True) -> pd.DataFrame:
    """Download adjusted close prices for all tickers. Cached to data/prices.csv."""
    import yfinance as yf

    cache_file = DATA_DIR / "prices.csv"
    if cache and cache_file.exists():
        return pd.read_csv(cache_file, index_col=0, parse_dates=True)

    raw = yf.download(
        list(TICKERS.values()), start=start, end=end,
        auto_adjust=True, progress=False,
    )["Close"]
    prices = raw.rename(columns={v: k for k, v in TICKERS.items()})[list(TICKERS)]
    prices = prices.dropna(how="all").ffill()

    if cache:
        DATA_DIR.mkdir(exist_ok=True)
        prices.to_csv(cache_file)
    return prices


def log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Daily log returns, first row dropped."""
    return np.log(prices / prices.shift(1)).dropna()


def data_quality_report(prices: pd.DataFrame) -> pd.DataFrame:
    """Simple checks to show model-validation discipline: gaps, stale prices, extremes."""
    rets = log_returns(prices)
    return pd.DataFrame({
        "first_date": prices.apply(lambda s: s.first_valid_index()),
        "n_obs": prices.count(),
        "n_missing": prices.isna().sum(),
        "n_zero_returns": (rets == 0).sum(),
        "max_abs_return": rets.abs().max(),
    })
