import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import re

products_df = pd.read_excel(
    "../data/ProductURL.xlsx"
)

amazon_df = products_df[
    products_df["Platform"].str.lower() == "amazon"
]

all_products = []

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    )

    for index, row in amazon_df.iterrows():

        brand = row["Brand"]
        url = row["URL"]

        if pd.isna(url) or str(url).strip() in ["", "-"]:

            print(
                f"\nSkipping invalid URL for {brand}"
            )

            continue

        print(
            f"\nScraping {brand}"
        )

        page = context.new_page()

        try:

            page.goto(
                str(url),
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(
                5000
            )

            html = page.content()

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            # PRODUCT NAME

            try:

                product_name = (
                    page.title()
                    .split(": Amazon")[0]
                    .strip()
                )

            except:

                product_name = "N/A"

            # CURRENT PRICE

            current_price = None

            try:

                price_element = page.locator(
                    ".a-price-whole"
                ).first

                current_price = float(
                    price_element
                    .text_content()
                    .strip()
                    .replace(",", "")
                )

            except:

                price_match = re.search(
                    r'"priceAmount":"?([0-9,.]+)',
                    html
                )

                if price_match:

                    current_price = float(
                        price_match.group(1)
                        .replace(",", "")
                    )

            # RATING

            try:

                rating = soup.find(
                    "span",
                    {
                        "data-hook":
                        "rating-out-of-text"
                    }
                ).text.strip()

            except:

                rating = None

            # REVIEWS

            try:

                reviews = soup.find(
                    "span",
                    {
                        "id":
                        "acrCustomerReviewText"
                    }
                ).text.strip()

            except:

                reviews = None

            product_data = {

                "timestamp":
                datetime.now(),

                "platform":
                "Amazon",

                "brand":
                brand,

                "product_name":
                product_name,

                "current_price":
                current_price,

                "rating":
                rating,

                "review_count":
                reviews,

                "url":
                url
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

final_df = pd.DataFrame(
    all_products
)

print(
    "\nTotal Scraped:"
)

print(
    len(final_df)
)

final_df.to_csv(
    "../data/amazon_products_day3.csv",
    index=False
)

print(
    "\nCSV Saved Successfully"
)