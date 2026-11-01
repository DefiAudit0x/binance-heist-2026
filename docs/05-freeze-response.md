# 05 · The Freeze Response — and the Gap

## What the issuers did

On the night of 10-29, Tether froze **~$1.6B USDT** and Circle **$800M+ USDC** — roughly half the loot, immobilized before it reached liquidity. This is the largest coordinated issuer freeze in the case's class.

## What the freeze did not do

Across 12 waves, every address discovered on the TRON machine was swept for `isBlackListed` via `triggerconstantcontract` on the native USDT contract. Running count:

| Wave | New checks | Cumulative |
|------|-----------|------------|
| 8 | 46 | 46/46 clean |
| 9 | 11 | 57/57 clean |
| 10 | 27 | 84/84 clean |
| 11 | 6 | 90/90 clean |
| 12 | 22 (incl. 8 new absorber callers) | **112/112 clean** |

On the EVM side, wave 12 checked all 7 mapped destinations directly on native USDT (`0xdAC17F…31ec7`) via `eth_call`: **0/7 blacklisted**. (The Arbitrum blacklist call reverted and is documented as an instrument limitation, not a result.)

## The disjoint-populations insight

The ~50% frozen and the ~50% moving are, so far, **two entirely different address populations**. Whatever the issuers froze on day one, the machine's visible layer never touched it. Two hypotheses are consistent with the data and are the subject of ongoing waves: (a) the frozen funds belong to the "slow" chains (BTC/XRP/SOL side and USDT held on non-TRON rails), and the TRON machine was built specifically to move the *unfreezable* half; (b) a second, still-unmapped layer exists between the machine and the frozen addresses. Nothing in the current evidence distinguishes them yet — and we say so.

## The remaining freeze surface

~**1.21M USDT** sleeping on `0xf78b2eda…` and `0x07ae8551…` is the last directly observable freeze candidate on the exit rail. The BTC (18,270.2004), XRP (233,461,943) and SOL (970,554) hoards remain static since the breach — they are the largest untouched remainder of the loot, and they are watched every three waves.
