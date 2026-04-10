#!/usr/bin/env python3
"""
Search Agent Skills Hub using Playwright (handles JavaScript rendering).

Install: pip install playwright && playwright install chromium
"""

import json
import asyncio
from playwright.async_api import async_playwright
import time

KEYWORDS = [
    "launch",
    "marketing",
    "distribution",
    "growth",
    "copywriting",
    "social media",
    "twitter",
    "product hunt",
    "landing page",
    "messaging",
    "positioning",
    "seo",
    "email"
]

BASE_URL = "https://agentskillshub.top"

async def search_keyword(keyword, page):
    """Search for a keyword and extract results."""
    print(f"\n🔍 Searching: {keyword}")

    search_url = f"{BASE_URL}/?s={keyword}"

    try:
        await page.goto(search_url, wait_until="networkidle", timeout=15000)
        await page.wait_for_timeout(2000)  # Wait for JS to render

        # Try to find skill/tool cards
        results = []

        # Common selectors for cards/items
        selectors = [
            'article',
            '.post',
            '.card',
            '.item',
            '[class*="skill"]',
            '[class*="tool"]'
        ]

        for selector in selectors:
            elements = await page.query_selector_all(selector)
            if elements:
                print(f"  Found {len(elements)} items with selector: {selector}")

                for elem in elements[:10]:  # Limit to first 10
                    try:
                        # Extract title
                        title_elem = await elem.query_selector('h2, h3, .title, [class*="title"]')
                        title = await title_elem.inner_text() if title_elem else None

                        # Extract description
                        desc_elem = await elem.query_selector('p, .description, [class*="desc"]')
                        description = await desc_elem.inner_text() if desc_elem else None

                        # Extract link
                        link_elem = await elem.query_selector('a')
                        link = await link_elem.get_attribute('href') if link_elem else None
                        if link and not link.startswith('http'):
                            link = f"{BASE_URL}{link}"

                        if title:
                            results.append({
                                'keyword': keyword,
                                'name': title.strip(),
                                'description': description.strip() if description else 'No description',
                                'link': link or 'No link',
                                'selector_used': selector
                            })
                    except:
                        continue

                if results:
                    break

        if not results:
            # Try to get page content for debugging
            content = await page.content()
            print(f"  ⚠️  No results parsed. Page has {len(content)} chars of HTML")

        return results

    except Exception as e:
        print(f"  ✗ Error: {str(e)[:100]}")
        return []

async def main():
    """Main search function."""
    print("=" * 70)
    print("Agent Skills Hub Search Tool (Playwright)")
    print("=" * 70)

    all_results = []

    async with async_playwright() as p:
        print("\n🚀 Launching browser...")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for keyword in KEYWORDS:
            results = await search_keyword(keyword, page)
            all_results.extend(results)
            await page.wait_for_timeout(1000)  # Be nice to the server

        await browser.close()

    # Remove duplicates
    unique_results = []
    seen_names = set()
    for result in all_results:
        if result['name'] not in seen_names:
            seen_names.add(result['name'])
            unique_results.append(result)

    # Save results
    output_file = 'agent-skills-hub-results.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_results, f, indent=2, ensure_ascii=False)

    # Print summary
    print("\n" + "=" * 70)
    print(f"✅ COMPLETE: Found {len(unique_results)} unique skills/tools")
    print("=" * 70)

    if unique_results:
        print("\n📋 Results:\n")
        for i, result in enumerate(unique_results, 1):
            print(f"{i}. {result['name']}")
            print(f"   Keyword: {result['keyword']}")
            desc = result['description']
            if len(desc) > 100:
                desc = desc[:100] + "..."
            print(f"   Description: {desc}")
            if result['link'] != 'No link':
                print(f"   Link: {result['link']}")
            print()

        # Categorize by keyword
        print("\n📊 Results by keyword:")
        keyword_counts = {}
        for result in unique_results:
            kw = result['keyword']
            keyword_counts[kw] = keyword_counts.get(kw, 0) + 1

        for kw, count in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {kw}: {count} results")
    else:
        print("\n⚠️  No results found")
        print("\nThis could mean:")
        print("1. No skills match these keywords")
        print("2. Site structure is different than expected")
        print("3. Need to adjust CSS selectors")
        print("\nRecommend: Manual search at https://agentskillshub.top/")

    print(f"\n💾 Results saved to: {output_file}")

if __name__ == "__main__":
    asyncio.run(main())
