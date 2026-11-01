# 04 · The Cross-Chain Exit (LayerZero OFT)

## Decoding the invisible

Wave 11 resolved the machine's selectors via the 4byte registry (`setDelegate`, `eid()`, `nextNonce`) and pinned the chain identities with LayerZero's **official metadata API**:

| eid | Chain | Sends (lifetime) | Lifetime USDT | Post-hack USDT |
|-----|-------|------------------|---------------|----------------|
| 30101 | Ethereum | 4,839 | $725,162,855.93 | $75,367,499.22 |
| 30110 | Arbitrum | 930 | $75,579,122.02 | $7,471,201.09 |
| 30343 | TON | 463 | $22,501,652.29 | $302,171.41 |
| 30168 | Solana | 332 | $12,836,481.06 | $316,379.21 |
| | **Total** | **6,564** | **$836,080,111.54** | **$83,457,251.12** |

- Lifetime window measured: **09-03 08:48 → 11-01 14:35 UTC** (bounded walk — the contract was born 08-12, so the lifetime figure is a **floor**).
- Post-hack window (≥ 10-29 20:04) is **fully covered** by the walk → that figure is **final**.
- Pre-hack throughput inside the window: ~**$752.6M** — the rail was doing $750M-scale business **before** the attack (its sibling `TNUNom8gxjz…` had already moved $100.84M in August). The machine is not a reaction to the hack; the hack intensified it.
- Post-hack rate ≈ **$565K/hour** at measurement time.

## Where it landed — and what happened next (wave 12, live)

| Destination (operator) | Received | Fate at 11-01 14:30 UTC |
|---|---|---|
| `0x5de841a6…894d6` (TB7) | $18.10M | **Drained** — swapped out via `0x6131B5fa…` on 10-31 22:00–22:06 |
| `0xf78b2eda…d6ce` (pay2) | $11.85M | **Holds 307,646.92 USDT + 104.88 ETH** — active at 14:31 |
| `0x12945c17…5453` (washer) | $9.69M | Drained — 0.001 USDT left |
| `0x07ae8551…70e67` (TAF) | $6.52M | **Holds 902,195.97 USDT** — `fillRelay` ×3 + `submitOrder` at 14:31 |
| `0xb7953595…43a04` ($5M single) | $5.00M | Drained 10-30 15:42 |
| `0x7f559a69…4e7e` (sibling) | $44.82M | Fully zeroed |
| `0x759ba420…2ad1` (Arbitrum) | $5.01M | **Still receiving** — +2,000 fresh USDT at 14:02:51 |

Patterns: funds do **not** sit. Four of seven drained within 24–48h through swaps and token transfers; ~**1.21M USDT** remains sleeping in two wallets — the last realistic freeze surface on this rail; one destination keeps absorbing fresh sends. Blacklist check via direct `eth_call` on native USDT: **0/7 blacklisted**.
