from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import os
import re

url = "https://www.croma.com/boat-nirvana-ion-anc-pro-tws-earbuds-with-active-noise-cancellation-ipx4-water-resistant-dual-eq-modes-crystal-black-/p/319481"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        viewport={"width": 1366, "height": 768}
    )

    page = context.new_page()

    print("Opening page...")

    try:

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(8000)

        print("Title:", page.title())

        html = page.content()

        with open("croma_page.html", "w", encoding="utf-8") as f:
            f.write(html)

        print("HTML Saved Successfully")

        soup = BeautifulSoup(html, "html.parser")

        # Product Name
        product_name = "N/A"

        h1 = page.locator("h1").first

        if h1.count() > 0:
            product_name = h1.text_content().strip()

        # Current Price
        current_price_num = None

        price = soup.find("span", {"id": "pdp-product-price"})

        if price:

            current_price_text = price.text.strip()

            current_price_num = float(
                current_price_text
                .replace("₹", "")
                .replace(",", "")
            )

        print("Current Price:", current_price_num)

        # Original Price (MRP)
        mrp_match = re.search(
            r'"mrp":\{"value":"([0-9.]+)"\}',
            html
        )

        if mrp_match:
            original_price = float(mrp_match.group(1))
        else:
            original_price = None

        print("Original Price:", original_price)

        # Discount %
        discount_percent = None

        if current_price_num and original_price:

            discount_percent = round(
                ((original_price - current_price_num)
                 / original_price) * 100,
                2
            )

        print("Discount %:", discount_percent)

        # Timestamp
        scrape_time = datetime.now()

        # Data Dictionary
        product_data = {
            "timestamp": scrape_time,
            "platform": "Croma",
            "brand": "boAt",
            "product_name": product_name,
            "current_price": current_price_num,
            "original_price": original_price,
            "discount_percent": discount_percent,
            "product_url": url
        }

        print("\nExtracted Data:")
        print(product_data)

        # Save CSV
        df = pd.DataFrame([product_data])

        csv_file = "croma_products.csv"

        if not os.path.exists(csv_file):
            df.to_csv(csv_file, index=False)
        else:
            df.to_csv(
                csv_file,
                mode="a",
                header=False,
                index=False
            )

        print("\nCSV Saved Successfully")

    except Exception as e:
        print("ERROR:", e)

    finally:
        browser.close()