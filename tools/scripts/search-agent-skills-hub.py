#!/usr/bin/env python3
"""
Search Agent Skills Hub for distribution/marketing related skills.

This script attempts to search agentskillshub.top for relevant skills.
May need adjustments based on site structure.
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin

# Keywords to search
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
    "email",
    "users",
    "acquisition"
]

BASE_URL = "https://agentskillshub.top"

def search_keyword(keyword, session):
    """Search for a specific keyword."""
    print(f"\n🔍 Searching for: {keyword}")

    # Try different possible search URL patterns
    possible_urls = [
        f"{BASE_URL}/search?q={keyword}",
        f"{BASE_URL}/search?keyword={keyword}",
        f"{BASE_URL}/skills?search={keyword}",
        f"{BASE_URL}/?s={keyword}",
    ]

    for url in possible_urls:
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                print(f"  ✓ Found results at: {url}")
                return parse_results(response.text, keyword)
        except Exception as e:
            continue

    print(f"  ✗ No results found")
    return []

def parse_results(html, keyword):
    """Parse search results from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    # Try to find skill cards/items
    # (These selectors are guesses - may need adjustment)
    skill_selectors = [
        '.skill-card',
        '.tool-card',
        '.item-card',
        'article',
        '.result-item',
    ]

    for selector in skill_selectors:
        items = soup.select(selector)
        if items:
            for item in items:
                # Try to extract name and description
                name = None
                description = None
                link = None

                # Try different patterns for name
                name_elem = (
                    item.select_one('h2') or
                    item.select_one('h3') or
                    item.select_one('.title') or
                    item.select_one('.name')
                )
                if name_elem:
                    name = name_elem.get_text(strip=True)

                # Try different patterns for description
                desc_elem = (
                    item.select_one('p') or
                    item.select_one('.description') or
                    item.select_one('.summary')
                )
                if desc_elem:
                    description = desc_elem.get_text(strip=True)

                # Try to find link
                link_elem = item.select_one('a')
                if link_elem and link_elem.get('href'):
                    link = urljoin(BASE_URL, link_elem['href'])

                if name:
                    results.append({
                        'keyword': keyword,
                        'name': name,
                        'description': description or 'No description',
                        'link': link or 'No link'
                    })

            if results:
                break

    return results

def main():
    """Main search function."""
    print("=" * 60)
    print("Agent Skills Hub Search Tool")
    print("Searching for distribution/marketing related skills...")
    print("=" * 60)

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })

    all_results = []

    for keyword in KEYWORDS:
        results = search_keyword(keyword, session)
        all_results.extend(results)
        time.sleep(1)  # Be respectful, don't hammer the server

    # Remove duplicates
    unique_results = []
    seen_names = set()
    for result in all_results:
        if result['name'] not in seen_names:
            seen_names.add(result['name'])
            unique_results.append(result)

    # Save results
    output_file = 'agent-skills-hub-results.json'
    with open(output_file, 'w') as f:
        json.dump(unique_results, f, indent=2)

    # Print summary
    print("\n" + "=" * 60)
    print(f"RESULTS: Found {len(unique_results)} unique skills")
    print("=" * 60)

    if unique_results:
        print("\n📋 Skills found:\n")
        for i, result in enumerate(unique_results, 1):
            print(f"{i}. {result['name']}")
            print(f"   Keyword: {result['keyword']}")
            print(f"   Description: {result['description'][:100]}...")
            if result['link'] != 'No link':
                print(f"   Link: {result['link']}")
            print()
    else:
        print("\n⚠️  No skills found.")
        print("\nPossible reasons:")
        print("1. Site uses JavaScript rendering (needs Selenium/Playwright)")
        print("2. Search URLs are different than expected")
        print("3. Site has anti-scraping measures")
        print("\nNext steps:")
        print("- Try manual search at: https://agentskillshub.top/")
        print("- Or we can use Playwright for JS rendering")

    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()
