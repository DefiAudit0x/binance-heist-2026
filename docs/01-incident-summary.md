# 01 · Incident Summary

**The breach.** Between 20:04 and 23:56 UTC on 2026-10-29, 17 Binance hot wallets were drained across 9 blockchains: approximately **$6.3 billion** in total — including 18,270.2004 BTC, 233,461,943 XRP, 970,554 SOL, and billions of USDT. From the first movement, the attacker's wallets fired sub-dollar "dust pings" between dozens of addresses, fragmenting the graph that analysts normally cluster on.

**The response.** Binance suspended withdrawals and on-chain containment began the same night. Tether froze approximately **$1.6 billion USDT** and Circle exceeded **$800 million USDC** — roughly half the loot — before it reached liquidity.

**The problem.** The other half concentrated on **TRON**, where no issuer freeze touched it. Over the following 51 hours, a purpose-built liquidation line ran: a distributor funded sweep wallets with **518.2M TRX**; a seller loop pushed TRX into a grid of pass-through lots at up to **26.2M TRX/hour**; and everything drained into a contract that had been sitting on TRON since at least August.

**The machine.** That contract — `TFG4wBa…` — looked like a SunSwap pair. It is not. It is a **custom UsdtOFT**: a LayerZero omnichain token contract whose bytecode contains **no ERC20 Transfer or Approval topics at all**. Value moves only through `send()` calldata, leaving **zero events** — invisible to every standard indexer. Three independent proofs established this (index gap, bytecode disassembly, empty transaction logs). Across its lifetime it has decoded **6,564 send() calls worth ≥ $836.08M** bridged to Ethereum, Arbitrum, TON and Solana — **$83.46M of it after the hack**, with the machine still firing live during our probes.

**The destinations.** On Ethereum, the mapped operator wallets mostly drained within 24–48 hours (via swaps and transfers); two still hold **1.21M USDT combined**, and one Arbitrum destination received fresh funds during the wave-12 probe. None of the seven is blacklisted on native USDT.

**The gap.** Across every address the machine touches — 112 of them as of wave 12 — **not one is frozen**. The frozen half and the moving half of this theft are disjoint populations. Dormant chains (BTC, XRP, SOL) have not moved since the breach.
