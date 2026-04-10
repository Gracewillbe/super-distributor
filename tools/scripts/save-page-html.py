#!/usr/bin/env python3
"""Save HTML from Agent Skills Hub search page for analysis."""

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Try to search for "launch"
        url = "https://agentskillshub.top/?s=launch"
        print(f"Loading: {url}")

        await page.goto(url, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(3000)  # Wait for JS to render

        # Save HTML
        html = await page.content()
        with open('agentskillshub-search-launch.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✅ Saved HTML ({len(html)} chars) to: agentskillshub-search-launch.html")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
