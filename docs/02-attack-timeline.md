# 02 · Attack Timeline

All times UTC. Evidence pointers refer to probe JSONs in the working repo and per-wave docs.

| Time | Event |
|------|-------|
| **2026-10-29 20:04** | First unauthorized movement from Binance hot wallets. Breach window opens. |
| 20:04 → 23:56 | 17 hot wallets drained across 9 chains ($6.3B est.). Dust-ping mesh starts fragmenting tracking. |
| 23:56 | Breach window closes. BTC (18,270.2004), XRP (233.46M), SOL (970,554) go **static** — they never move again through wave 12. |
| **Night 10-29** | Binance halts withdrawals. Tether freezes ~$1.6B USDT; Circle freezes $800M+ USDC (≈50% of loot). |
| **2026-10-30 (wave 1)** | Main TRX treasury **emptied in full** — captured live while monitored. |
| 10-30 10:18–10:19 | Distributor `41b8db53…` funds 3 sweep wallets × 120,000,000 TRX (518.2M TRX vault layer). |
| 10-30 → 10-31 | Seller loop `TRBdWqHn…` pushes TRX into 20+ pass-through lots; SunSwap pair side shows skim-style USDT extraction (−7.15M measured in wave 7). |
| **10-31 18:44:36** | Last intact sweep vault emptied (tx `e8441d62…`). All 518.2M TRX now inside the machine. |
| 10-31 (wave 8) | Seller at peak: 219.08M TRX out in 8.4h = 26.2M/h. New selling pools spin up; freeze sweep 46/46 clean. |
| **11-01 00:48 → 05:35** | Final seller drain: 21 legs / 21.11M, then 35 legs / 21.74M. Machine decelerates to 6.32M/h, then stops. |
| 11-01 05:35:18 | **Seller's last transaction.** Balance: 131.004037 TRX. The loop is dry; accounting closes to fees (−15.97 TRX). |
| 11-01 (waves 9–11) | Machine identity decoded: custom **UsdtOFT**; spender == absorber; 1,100 sends = $132.94M decoded; eids pinned via LayerZero metadata. |
| 11-01 13:36:36 | Last send measured by wave 11. Freeze cumulative 90/90. |
| **11-01 13:45 → 14:40 (wave 12)** | Lifetime walk: 6,564 sends / $836.08M (floor, since 09-03); post-hack $83.46M final. EVM destination fates resolved. |
| **11-01 14:35:39** | **Live capture:** the absorber fires 30,050 USDT to Ethereum *while the probe is running*. Machine confirmed alive. |
