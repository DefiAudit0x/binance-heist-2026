# Twitter/X thread — ready to post

> Data-checked against README (through 2026-11-01 14:40 UTC). Attach the matching exhibit to each tweet.

**1/12** 🚨 On Oct 29, 2026, $6.3 BILLION was lifted from 17 Binance hot wallets across 9 chains in 3h 52m.

We've been tracking the aftermath live for 12 straight waves — using nothing but public blockchain data.

This is what the money did. 🧵
#Binance #CryptoHack #OnChainAnalysis

**2/12** The freeze wall came fast: Tether froze ~$1.6B USDT, Circle $800M+ USDC — roughly HALF the loot.

The other half went where issuers can't reach: TRON. [attach 01_timeline.png]
#Tether #USDT #Tron

**3/12** First move: a distributor funded sweep wallets with 518.2M TRX. A seller loop pushed it out at up to 26.2M TRX/hour through a grid of pass-through lots.

By Nov 1, 05:35 UTC the loop was DRY — 131.004037 TRX left. Accounting closed to fees.
#BlockchainForensics

**4/12** The core of the machine: contract TFG4wBa… looked like a SunSwap pair.

It's not. It's a custom UsdtOFT — a LayerZero omnichain token with ZERO ERC20 Transfer/Approval topics in its bytecode.

Value moves only in calldata. Invisible to standard indexing. [attach 02_fund_flow.png]
#LayerZero #OFT

**5/12** We decoded it anyway: 6,564 send() calls = $836.08 MILLION bridged to Ethereum ($725.2M), Arbitrum ($75.6M), TON ($22.5M), Solana ($12.8M) — since Sep 3.

$752.6M of that was BEFORE the hack. The machine predates the heist.
#CryptoForensics

**6/12** $83,457,251 crossed those chains AFTER the hack — a final, fully-covered window. ≈$565K/hour.

And the last send fired at 14:35:39 UTC — WHILE our probe was running. The machine is still alive. [attach 04_absorber_lifetime.png]
#IncidentResponse

**7/12** Where did it land? Operator wallets on Ethereum:

• 4 of 7 drained within 24–48h (swaps + transfers)
• 2 still hold 1.21M USDT combined
• 1 (Arbitrum) received FRESH funds during our probe

0/7 blacklisted on native USDT. [attach 03_status_board.png]
#ThreatIntel

**8/12** The uncomfortable finding: across 112 addresses this machine touches — ALL freeze-clean.

The frozen half and the moving half of this theft are two disjoint populations. The issuer wall never touched this rail.
#Tether #Stablecoin

**9/12** Meanwhile the "slow" loot never moved: 18,270.2 BTC + 233.5M XRP + 970,554 SOL — zero movement since the breach, watched every 3 waves.

The biggest untouched chunk of the $6.3B is sitting still. #OSINT

**10/12** How do you verify an "invisible" machine? Three independent proofs:
• ≥$54.13M missing from the TRC20 index
• no event topics in the bytecode
• empty logs on successful sends

Triple-consistent. Only calldata remains. #OpenSourceIntel

**11/12** Full honesty ledger published: every self-caught error corrected in writing — including a TronGrid pagination bug that produced phantom future-dated transactions (proven fake, re-measured).

Reproducible exhibits + data included.
#Transparency

**12/12** Full dossier: README, minute-level timeline, machine anatomy, destination fates, freeze analysis, methodology, data (CSV), wave log W1–W12.

⭐ https://github.com/DefiAudit0x/binance-heist-2026

#Binance #CryptoHack #OnChainAnalysis #BlockchainForensics #Tron #USDT #LayerZero #OSINT #ThreatIntel #IncidentResponse #Stablecoin #SecurityResearch
