# 06 · Methodology & Integrity

## Data sources (all public)

- **TronGrid** — native transaction walks, TRC20 walks by contract fingerprint, `triggerconstantcontract` for freeze checks, `gettransactioninfobyid` for log inspection.
- **Blockscout v2** (eth + arb) — address info, transactions, token transfers.
- **Direct `eth_call`** via public RPC — `balanceOf` / `isBlackListed` on native USDT (selector sanity-checked: `balanceOf` = `70a08231`; `isBlackListed` computed by keccak at runtime).
- **LayerZero official metadata API** — eid → chain identity pinning.
- **4byte.directory** — selector identification.

## Techniques

1. **Bounded fingerprint walks** with explicit windows and declared page caps. Every total is labeled **floor** unless the window is provably complete.
2. **ABI decoding of calldata** — the machine's only footprint.
3. **Accounting closure** — every balance delta must reconcile to fees or be explained by a found transaction (e.g., the wave-11 boundary sweep that resolved a −355,076 TRX delta to two pre-cutoff legs + 15.97 fees).
4. **Differential baselining** — each wave starts from the previous wave's published state; every address carries forward.
5. **Live capture discipline** — probes run against the chain tip; anything observed *during* a probe is marked as such.

## The honesty ledger (self-caught errors, corrected pre-delivery)

| # | Error caught | Correction |
|---|--------------|------------|
| B11 | eid map initially guessed 30101 = Solana | Official LayerZero metadata: 30101 = **Ethereum**, 30168 = Solana, 30343 = TON; aggregation re-derived per (eid, address) |
| B11 | Zero-ping counter compared floats exactly | 40 × 2-SUN pings counted correctly |
| B12 | **TronGrid ascending-fingerprint walk invalid** | Produced mid-walk page drops (1,071 vs 4,194 sends in the same overlap window) **and a phantom future-dated tail** (1,399 rows up to "12-22"). Proven fake: descending walk with `min_timestamp` sees nothing after 14:35:39; phantom txid prefix absent from newest 200 real txs. Lifetime re-measured with a deep **descending** walk (monotonic, zero future rows). **Lesson: never use asc+fingerprint on high-volume TronGrid accounts.** |
| B12 | Pulse counter compared "MM-DD" strings to a full-date literal | Recomputed with parsed timestamps |
| B12 | eid 30125 absent from official metadata | Excluded from clean tables, noted only |
| (earlier) | TronScan `accountv2` 401 / 422-with-params on Blockscout / arb 404 | Documented; balances via direct `eth_call`; walks via TronGrid |

## Reproducibility

Every exhibit regenerates from `exhibits/src/` (HTML/CSS + a Playwright/matplotlib render script). Probe JSONs are stored per wave in the working repo (`data/binance/waveN_probe*.json`) and linked from the wave log. No number in this repository exists without a stored, re-runnable query behind it.
