from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

url = "https://www.flipkart.com/boat-nirvana-ion-anc-pro-w-hi-res-audio-ldac-anc-120h-battery-multi-connect-bluetooth/p/itm10c05fa3e3741"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()

    page.goto(
        url,
        wait_until="networkidle",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    html = page.content()

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    scripts = soup.find_all(
        "script",
        type="application/ld+json"
    )

    for script in scripts:

        try:

            data = json.loads(
                script.string
            )

            if isinstance(data, list):

                for item in data:

                    if item.get("@type") == "Product":

                        print("\n===== PRODUCT DETAILS =====")

                        print(
                            "Product Name :",
                            item.get("name")
                        )

                        print(
                            "Brand :",
                            item.get("brand", {})
                            .get("name")
                        )

                        print(
                            "Current Price :",
                            item.get("offers", {})
                            .get("price")
                        )

                        print(
                            "Rating :",
                            item.get("aggregateRating", {})
                            .get("ratingValue")
                        )

                        print(
                            "Reviews :",
                            item.get("aggregateRating", {})
                            .get("reviewCount")
                        )

        except:
            pass

    browser.close()