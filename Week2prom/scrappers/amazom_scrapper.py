from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

url = "https://www.amazon.in/Nirvana-Battery-Bluetooth-Wireless-Earphones/dp/B0FP9DP8FH"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    )

    page = context.new_page()

    print("Opening Amazon Product Page...")

    page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    html = page.content()

    with open(
        "amazon_page.html",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(html)

    print("HTML Saved Successfully")

    print(page.title())

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    print("\nSearching Product Details...")

    # PRODUCT NAME
    try:
        product_name = page.title().split(": Amazon")[0].strip()
    except:
        product_name = "N/A"

    # CURRENT PRICE
    current_price = "N/A"

    try:
        price_element = page.locator(
            ".a-price-whole"
        ).first

        current_price = (
            price_element.text_content()
            .strip()
            .replace(",", "")
        )

    except:

        price_match = re.search(
            r'"priceAmount":"?([0-9,.]+)',
            html
        )

        if price_match:
            current_price = (
                price_match.group(1)
                .replace(",", "")
            )

    # RATING
    try:
        rating = soup.find(
            "span",
            {"data-hook": "rating-out-of-text"}
        ).text.strip()

    except:
        rating = "N/A"

    # REVIEWS
    try:
        reviews = soup.find(
            "span",
            {"id": "acrCustomerReviewText"}
        ).text.strip()

    except:
        reviews = "N/A"

    print("\n===== PRODUCT DETAILS =====")
    print("Product Name :", product_name)
    print("Current Price:", current_price)
    print("Rating       :", rating)
    print("Reviews      :", reviews)

    browser.close()