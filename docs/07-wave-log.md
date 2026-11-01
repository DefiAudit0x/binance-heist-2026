# 07 · Wave Log (W1–W12)

The investigation proceeds in **waves**: each wave re-measures the live state, extends the graph, closes its accounting, and publishes evidence before the next one starts.

| Wave | When (UTC) | Headline results |
|------|------------|------------------|
| **W1** | 10-29/30 | Breach scoped (17 wallets / 9 chains / $6.3B est.). **Main TRX treasury emptied live** under monitoring — the first "live catch". |
| **W2–W3** | 10-30 | TRON layer mapped. Differential baseline set: distributor `41b8db53…` → 4 sweep wallets (**518.2M TRX**); seller loop `TRBdWqHn…` ramping; SunSwap pair `TFG4wBa…` USDT side 53.05M → 51.89M; static chains confirmed (BTC/XRP/SOL/ARB). Next-wave plan published. |
| **W4–W6** | 10-30/31 | Vault and lot census deepened. *(The early case folder was lost in a session incident — disclosed at wave 7; results survive through the baselines carried by later waves.)* |
| **W7** | 10-31 | Live probe: **120M TRX relay cadence (~7h)** hash-pinned ×3; pair skimmed **−7.15M USDT** skim-style while its TRX side stood still; sweep-1 last intact vault. |
| **W8** | 10-31 | **Last vault falls 18:44:36** (tx `e8441d62…`) — full 518.2M inside the machine; seller 219.08M out @ 26.2M/h; selling moves to new pools; freeze 46/46. |
| **W9** | 11-01 | Absorber decoded: **not a pair** (no getReserves/token0/token1); spender == absorber (86 approvals / 28 wallets, ×3 drain-eve allowances consumed); **≥ $54,126,799.56 missing from the TRC20 index with zero events**; freeze 57/57. |
| **W10** | 11-01 | Bytecode named: **UsdtOFT**, 22,646 B, hash `e5286143` — **no standard ERC20 Transfer/Approval topics anywhere**; seller depleted 43.20M → 22.10M TRX via 21 legs; **pay1 = $2.34B pre-hack hub**; pool-B funding map (255 legs / 70 funders); freeze 84/84. |
| **W11** | 11-01 | **1,100 send() calls ABI-decoded = $132,940,089.98** (ETH $122.47M / ARB $9.07M / SOL $1.08M / TON $317K), eids pinned from LayerZero metadata; operator map 1:1 (TB7→0x5de841a6 $18.10M, pay2→0xf78b2eda $11.85M, washer→0x12945c17 $9.69M, TAF→0x07ae8551 $6.52M); **seller DRY at 131.004037** (accounting closed to −15.97 fees); **sibling UsdtOFT $100.84M in August**; `TKy1L5rak` perfect loop $1.064B; **empty logs on successful sends** = third proof of invisibility; freeze 90/90. |
| **W12** | 11-01 | **Lifetime $836,080,111.54 / 6,564 sends** (deep descending walk; floor since 09-03, born 08-12); **post-hack $83,457,251.12 / 803 — final** (window fully covered); destination fates resolved (4/7 drained, 2 holding 1.21M, 1 receiving fresh); **live capture 14:35:39 during probe**; new micro-operators; TB7 = zero-balance pass-through; giants measured (TKHuVq1o $11.71B/$10.44B); freeze **112/112**. |

## Open leads (wave 13 queue)

1. Identify treasury giants `TETzqWSBDY12…` ($7.50B sink) and `TBPxhVAsuzoF…` ($4.00B feeder) via exchange deposit-address fingerprints.
2. Pin the EVM contracts used for disposal (`0x6131B5fa…` swaps, `0x5c7BCd6E…` fillRelay, `0x49AAA987…` submitOrder).
3. Watch the 1.21M sleeping USDT on `0xf78b2eda…` / `0x07ae8551…`.
4. Profile the new micro-operators (TYmHwFmjngMB, TFNPHPpHQX, TXAQd3BhC3, TSMtAweHkM, THLTgNbHXx).
5. Extend the lifetime walk to the contract's birth (08-12) — the gap above $836.08M.
6. Recurring freeze sweeps + three-wave dormancy recheck on BTC/XRP/SOL.
