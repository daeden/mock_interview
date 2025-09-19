#!/usr/bin/env python3
"""
MUNI BOND – RESEARCH ENGINEERING EXERCISE (SKELETON)
Timebox: ~2 hours

Implement the TODOs. Keep code concise and readable.
You may add helper functions/classes and brief docstrings as needed.
"""

from __future__ import annotations
import math
from dataclasses import dataclass
from datetime import date, datetime
from typing import Iterable, Tuple, Dict
import pandas as pd

SETTLEMENT_DATE = date(2025, 9, 17)

# ---------- 1) ETL ----------

def load_and_clean(muni_csv: str, tsy_csv: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    TODO:
      - Read the two CSVs.
      - Parse dates.
      - Drop obviously bad rows (e.g., missing price, maturity in the past).
      - Return cleaned dataframes (muni, tsy).
    """
    raise NotImplementedError


# ---------- 2) FIXED INCOME MATH ----------

def year_fraction(d1: date, d2: date, basis: str = "act/365") -> float:
    """
    TODO:
      - Implement at least one daycount (act/365 or 30/360).
      - Keep it simple and documented.
    """
    raise NotImplementedError

def ytm(price: float, coupon_pct: float, maturity: date, settlement: date = SETTLEMENT_DATE, freq: int = 2) -> float:
    """
    TODO:
      - Compute Yield-To-Maturity (annualized %, simple Newton-Raphson is fine).
      - Assume bullet, level coupons, ignore taxes/calls.
      - Hint: cashflows each period until maturity; solve PV(cashflows) = price.
    """
    raise NotImplementedError

def price_from_ytm(yield_pct: float, coupon_pct: float, maturity: date, settlement: date = SETTLEMENT_DATE, freq: int = 2) -> float:
    """
    TODO:
      - Given a yield (%), return clean price per 100.
    """
    raise NotImplementedError


# ---------- 3) ANALYSIS ----------

def maturity_bucket(years_to_mat: float) -> str:
    """Return '1–5y', '5–10y', or '10y+' based on years_to_mat."""
    if years_to_mat <= 5: return "1–5y"
    if years_to_mat <= 10: return "5–10y"
    return "10y+"

def closest_tenor(years: float, tenor_list: Iterable[float]) -> float:
    """Return tenor with minimal absolute difference from 'years'."""
    return min(tenor_list, key=lambda t: abs(t - years))

def compute_spreads(muni: pd.DataFrame, tsy: pd.DataFrame) -> pd.DataFrame:
    """
    TODO:
      - For each bond, compute YTM.
      - Map to closest treasury tenor and compute Spread (muni_yield - tsy_yield) in bps.
      - Return a per-bond DataFrame with columns:
          ['CUSIP','YearsToMat','Bucket','MuniYTM%','TsyYield%','Spread_bps']
    """
    raise NotImplementedError

def summarize_spreads(per_bond: pd.DataFrame) -> pd.DataFrame:
    """
    TODO:
      - Group by Bucket and produce:
          Avg_MuniYTM_pct, Avg_TsyYield_pct, Avg_Spread_bps, N
    """
    raise NotImplementedError

def stress_parallel_shift(muni: pd.DataFrame, shift_bps: float = 100.0) -> pd.DataFrame:
    """
    TODO:
      - Shift each bond's YTM by +shift_bps and recompute price.
      - Report % price change by bond and summarize by bucket.
      - Return summary DataFrame with columns:
          ['Bucket','Avg_PctChange_pct','N']
    """
    raise NotImplementedError


# ---------- 4) CLI ENTRY ----------

def main() -> None:
    import argparse
    p = argparse.ArgumentParser(description="Muni Bond Research Exercise")
    p.add_argument("--muni", default="muni_bonds_sample.csv")
    p.add_argument("--tsy", default="treasury_yields_sample.csv")
    p.add_argument("--shift_bps", type=float, default=100.0)
    args = p.parse_args()

    muni, tsy = load_and_clean(args.muni, args.tsy)

    per_bond = compute_spreads(muni, tsy)
    spread_summary = summarize_spreads(per_bond)
    stress_summary = stress_parallel_shift(muni, shift_bps=args.shift_bps)

    print("=== Spread Summary by Bucket ===")
    print(spread_summary.to_string(index=False))
    print("\n=== Stress Summary by Bucket (+" + str(int(args.shift_bps)) + " bps) ===")
    print(stress_summary.to_string(index=False))

if __name__ == "__main__":
    main()
