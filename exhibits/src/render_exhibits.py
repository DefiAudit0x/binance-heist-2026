#!/usr/bin/env python3
"""Render publication exhibits: 4 CSS boards (Playwright) + 1 matplotlib data chart.
Output -> /home/z/my-project/download/binance-heist-2026/exhibits/"""
import asyncio, os
from playwright.async_api import async_playwright

SRC = "/home/z/my-project/scripts/pubsrc"
OUT = "/home/z/my-project/download/binance-heist-2026/exhibits"
os.makedirs(OUT, exist_ok=True)

async def shot(html, png, selector="#root", width=1300, scale=2):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": width, "height": 900}, device_scale_factor=scale)
        await page.goto(f"file://{html}", wait_until="networkidle")
        await page.wait_for_timeout(500)
        el = page.locator(selector)
        bbox = await el.bounding_box()
        if bbox:
            await page.set_viewport_size({"width": max(width, int(bbox["width"] + 60)),
                                          "height": int(bbox["height"] + 80)})
            await page.wait_for_timeout(250)
        await el.screenshot(path=png)
        await browser.close()
    print(f"OK {png} ({os.path.getsize(png)/1024:.0f} KB)")

async def css_batch():
    for name, w in (("00_hero", 1680), ("01_timeline", 1300), ("02_fund_flow", 1340), ("03_status_board", 1300)):
        await shot(f"{SRC}/{name}.html", f"{OUT}/{name}.png", width=w)

def mpl_chart():
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({
        "font.sans-serif": ["DejaVu Sans"], "axes.unicode_minus": False,
        "figure.facecolor": "#FFFFFF", "axes.facecolor": "#FFFFFF",
        "axes.edgecolor": "#E5E7EB", "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "xtick.major.size": 0, "ytick.major.size": 0,
        "xtick.labelsize": 11, "ytick.labelsize": 11,
        "legend.frameon": False, "figure.dpi": 200, "savefig.dpi": 200,
    })
    G900, G500, G400 = "#111827", "#6B7280", "#9CA3AF"
    ACCENT, MUTED = "#2563EB", "#D6DEE8"

    chains = ["Ethereum", "Arbitrum", "TON", "Solana"]
    lifetime = [725.16, 75.58, 22.50, 12.84]
    posthack = [75.37, 7.47, 0.302, 0.316]
    n_sends = ["4,839", "930", "463", "332"]

    x = np.arange(len(chains)); w = 0.38
    fig, ax = plt.subplots(figsize=(13.2, 6.6), constrained_layout=True)
    b1 = ax.bar(x - w/2, lifetime, w, color=MUTED, label="Lifetime since Sep 3 (floor)", zorder=3)
    b2 = ax.bar(x + w/2, posthack, w, color=ACCENT, label="After the hack (Oct 29 20:04 →)", zorder=3)
    for b, v in zip(b1, lifetime):
        ax.text(b.get_x() + b.get_width()/2, v + 12, f"${v:,.1f}M", ha="center", fontsize=10.5,
                fontweight="bold", color=G500)
    for b, v, n in zip(b2, posthack, n_sends):
        ax.text(b.get_x() + b.get_width()/2, v + 12, f"${v:,.1f}M", ha="center", fontsize=10.5,
                fontweight="bold", color=ACCENT)
    for xi, n in zip(x, n_sends):
        ax.text(xi - w/2, 22, f"{n} sends", ha="center", fontsize=9.5, color=G900, rotation=0)
    ax.set_xticks(x); ax.set_xticklabels(chains, fontsize=12)
    ax.set_ylabel("USDT bridged out (millions)")
    ax.set_ylim(0, max(lifetime) * 1.2)
    ax.set_title("The wash machine's OFT exit by chain — absorber TFG4wBa (UsdtOFT)\n"
                 "6,564 sends = $836.08M lifetime since 09-03 (floor); $83.46M of it after the hack (final)",
                 fontsize=14, fontweight="bold", loc="left", color=G900, pad=14)
    ax.legend(loc="upper right", fontsize=11)
    ax.yaxis.grid(True, alpha=0.15, zorder=0)
    ax.text(0.995, -0.13, "Source: deep desc walk 45pp × 200 tx, monotonic, zero phantom rows — data/binance/wave12_lifetime_authoritative.json",
            transform=ax.transAxes, ha="right", fontsize=9, color=G400)
    out = f"{OUT}/04_absorber_lifetime.png"
    fig.savefig(out, dpi=200, facecolor="white")
    plt.close(fig)
    print(f"OK {out} ({os.path.getsize(out)/1024:.0f} KB)")

if __name__ == "__main__":
    asyncio.run(css_batch())
    mpl_chart()
