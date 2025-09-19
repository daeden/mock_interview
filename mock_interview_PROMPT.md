# Muni Bond – Research Engineering Exercise (2 hours)

**Context (startup muni fund):** We need a quick, pragmatic tool that helps us understand muni bond yields and how they move vs Treasuries. You’ll implement a small pipeline + analysis, then explain the results like you would to a PM.

## Provided
- `muni_bonds_sample.csv` — fields: CUSIP, Issuer, MaturityDate, CouponRate, Price, Rating, IssueDate
- `treasury_yields_sample.csv` — snapshot of Treasury tenors & yields
- `mock_interview_skeleton.py` — incomplete scaffold with TODOs

> You may add helper functions; keep scope reasonable. Don’t over-engineer.

## Tasks
1) **ETL**  
   Load the CSVs, parse dates, and drop obvious bad rows (e.g., missing prices, maturities in the past).

2) **Fixed-Income Math**  
   Implement:
   - `year_fraction` (pick a basis and document it)
   - `ytm` via a simple solver (Newton–Raphson is fine). Assumptions: bullet, level coupons, ignore taxes/calls.
   - `price_from_ytm` (clean price per 100)

3) **Spreads vs Treasury**  
   For each muni, compute YTM and map to the closest Treasury tenor. Compute **Spread = muni_yield − treasury_yield** in **bps**. Produce both per‑bond results and a **bucket summary** (1–5y, 5–10y, 10y+).

4) **+100 bps Parallel Shift Stress**  
   Shift each bond’s yield up by +100 bps, recompute price, and summarize average % price change by bucket.

5) **Takeaways (written, 5–10 sentences)**  
   In plain English, explain what the numbers imply for a muni portfolio (e.g., where spreads are wider/tighter, which buckets are most price‑sensitive, any data issues).

## Stretch (if time remains)
- Compute a rough **modified duration** from your pricing function and reconcile with your stress result.
- Add **Tax-Equivalent Yield** assuming a given marginal tax rate; discuss why it matters for munis.
- Add a **rating bucket** view (e.g., AA and above vs A and below) and comment on spread differences.

## What we evaluate
- **Practical programming:** clean, modular code; handling messy data; sensible assumptions.
- **FI intuition:** correct directionality; units (bps vs %); maturity vs sensitivity.
- **Communication:** short, clear takeaway suited for a PM/PMO discussion.

## How to run
```bash
python mock_interview_skeleton.py --muni muni_bonds_sample.csv --tsy treasury_yields_sample.csv --shift_bps 100
```
