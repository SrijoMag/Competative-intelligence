import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import json

products_df = pd.read_excel("../data/ProductURL.xlsx")

flipkart_df = products_df[
    products_df["Platform"].str.lower() == "flipkart"
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

    for index, row in flipkart_df.iterrows():

        brand = row["Brand"]
        url = row["URL"]

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

            product_name = "N/A"
            current_price = None
            original_price = None
            rating = None
            review_count = None

            scripts = soup.find_all(
                "script",
                type="application/ld+json"
            )

            for script in scripts:

                try:

                    if not script.string:
                        continue

                    data = json.loads(
                        script.string
                    )

                    if isinstance(data, list):
                        data = data[0]

                    if (
                        isinstance(data, dict)
                        and data.get("@type") == "Product"
                    ):

                        product_name = data.get(
                            "name",
                            "N/A"
                        )

                        current_price = data.get(
                            "offers",
                            {}
                        ).get(
                            "price"
                        )

                        rating = data.get(
                            "aggregateRating",
                            {}
                        ).get(
                            "ratingValue"
                        )

                        review_count = data.get(
                            "aggregateRating",
                            {}
                        ).get(
                            "reviewCount"
                        )

                        break

                except:
                    pass

            product_data = {

                "timestamp": datetime.now(),
                "platform": "Flipkart",
                "brand": brand,
                "product_name": product_name,
                "current_price": current_price,
                "original_price": original_price,
                "discount_percent": None,
                "rating": rating,
                "review_count": review_count,
                "url": url

            }

            print(product_data)

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

    browser.close()

final_df = pd.DataFrame(all_products)

print("\nTotal Scraped:")
print(len(final_df))

try:

    final_df.to_csv(
        "../data/flipkart_products_day3_new.csv",
        index=False
    )

    print(
        "\nCSV Saved Successfully"
    )

except Exception as e:

    print(
        "\nCould not save CSV"
    )

    print(e)