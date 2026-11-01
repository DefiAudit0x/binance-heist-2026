# 03 · The Wash Machine (TRON Anatomy)

## Layer 1 — Vault

Distributor `41b8db53…` funded three sweep wallets at 120,000,000 TRX each on 10-30 10:18–10:19 (a fourth, `TKkH2vH6…`, held 158,200,902). Total: **518.2M TRX**. The vaults fell one by one — the last at **10-31 18:44:36** (tx `e8441d62…`) — feeding everything into the machine.

## Layer 2 — Seller loop

`TRBdWqHnDVSZCVGfgHdKFLQPirQcA2PRki` (born 10-30 00:06) was the TRX disposal engine:

| Phase | Behaviour |
|---|---|
| Ramp (10-30) | Multi-million TRX legs into the lot grid; measured 26.2M TRX/h at peak |
| Sprint (10-31 → 11-01 05:35) | 21.74M TRX pushed in 35 legs in the final window (6.32M/h, decelerating) |
| Death (11-01) | **Dry at 131.004037 TRX**; zero native activity since 05:35:18; accounting closed to fees |

Dozens of 2-SUN zero-value pings interleaved the drain — the same anti-tracking mesh seen across the case. The lot grid (20+ wallets) passed TRX straight through with zero retained balances.

## Layer 3 — The absorber

`TFG4wBaDQ8sHWWP1ACeSGnoNR6RRzevLPt` was catalogued as a "SunSwap pair" in wave 3. Waves 9–10 proved it is neither: it has no `getReserves`, no `token0`/`token1` — its bytecode (22,646 B, code-hash `e5286143`) declares a **UsdtOFT**: an omnichain fungible token in the LayerZero V2 pattern. Its dominant selector is `c7c7f5b3` = `send((uint32,bytes32,uint256,uint256,bytes,bytes,bytes),(uint256,uint256),address)`.

**Why nothing shows in any explorer:** the bytecode contains **no ERC20 Transfer/Approval event topics at all**. Successful `send()` transactions return **empty logs**. The TRC20 index is missing ≥ $54.13M of realized outflow. The machine is visible **only in calldata** — which is where wave 12 measured its full lifetime.

## The feeders

Callers with a 1:1 operator map to EVM destinations (see doc 04): `TB7pUXyw…` (unlimited MaxUint256 USDT approval to the absorber), `TVXxphhF…` (pay2), `TMKcUby8…` (washer), `TAfpoKQJ…`, plus 12+ micro-operators discovered in wave 12 — the newest (`TYmHwFmjngMB`) fired during our probe.

## Parallel structure (pre-existing)

A separate treasury cluster ran before and after the hack: `pay1 TQecYjXd…` ($2.34B hub since 05-30) → perfect loop `TKy1L5rak` (152 in / 152 out = $1.064B, zero delta) → bidirectional core `TXFBqBbq` → treasury-scale `TKHuVq1o` (**$11.71B in / $10.44B out**, platform-pattern round-number flows with 20/39 unique counterparties). Its top sink `TETzqWSBDY12…` ($7.50B) and top external feeder `TBPxhVAsuzoF…` ($4.00B) are the wave-13 identification targets.
