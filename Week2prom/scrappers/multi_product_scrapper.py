import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import re

products_df = pd.read_excel("../data/ProductURL.xlsx")

croma_df = products_df[
    products_df["Platform"].str.lower() == "croma"
]

all_products = []

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0"
    )

    for index, row in croma_df.iterrows():

        brand = row["Brand"]
        url = row["URL"]

        # Skip invalid URLs
        if pd.isna(url) or str(url).strip() in ["", "-"]:
            print(f"\nSkipping invalid URL for {brand}")
            continue

        print(f"\nScraping {brand}")

        page = context.new_page()

        try:

            page.goto(
                str(url),
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(5000)

            html = page.content()

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            h1 = page.locator("h1").first

            if h1.count() > 0:
                product_name = h1.text_content().strip()
            else:
                product_name = "N/A"

            price = soup.find(
                "span",
                {"id": "pdp-product-price"}
            )

            if price:

                current_price = float(
                    price.text.strip()
                    .replace("₹", "")
                    .replace(",", "")
                )

            else:
                current_price = None

            mrp_match = re.search(
                r'"mrp":\{"value":"([0-9.]+)"\}',
                html
            )

            if mrp_match:
                original_price = float(
                    mrp_match.group(1)
                )
            else:
                original_price = None

            discount_percent = None

            if current_price and original_price:

                discount_percent = round(
                    (
                        (original_price - current_price)
                        / original_price
                    ) * 100,
                    2
                )

            product_data = {

                "timestamp": datetime.now(),
                "platform": "Croma",
                "brand": brand,
                "product_name": product_name,
                "current_price": current_price,
                "original_price": original_price,
                "discount_percent": discount_percent,
                "url": url
            }

            all_products.append(
                product_data
            )

            print(
                f"Success: {product_name}"
            )

        except Exception as e:

            print(
                f"Failed: {url}"
            )

            print(e)

        finally:

            page.close()

    try:
        browser.close()
    except:
        pass

final_df = pd.DataFrame(all_products)

print("\nTotal Scraped:")
print(len(final_df))

final_df.to_csv(
    "../data/croma_products_day3.csv",
    index=False
)

print(
    "\nCSV Saved Successfully"
)