import pandas as pd
from config import *

print("Loading Dashboard Dataset...")

df = pd.read_csv("outputs\dashboard_dataset.csv")
total_products = len(df)
avg_price = round(df["current_price"].mean(), 2)
avg_rating = round(df["rating"].mean(), 2)
avg_discount = round(df["discount_percent"].mean(), 2)
avg_opportunity = round(df["opportunity_score"].mean(), 2)

recommendations = df["final_recommendation"].value_counts()
priority = df["priority"].value_counts()
platform = df.groupby("platform")["current_price"].mean()
brand = (
    df.groupby("brand")["opportunity_score"]
    .mean()
    .sort_values(ascending=False)
)
top_products = df.sort_values(
    by="priority_score",
    ascending=False
).head(10)


with open(EXECUTIVE_SUMMARY, "w", encoding="utf-8") as file:

    file.write("="*60 + "\n")
    file.write("WEEK 6 EXECUTIVE SUMMARY\n")
    file.write("="*60 + "\n\n")

    file.write(f"Total Products : {total_products}\n")
    file.write(f"Average Price : ₹{avg_price}\n")
    file.write(f"Average Rating : {avg_rating}\n")
    file.write(f"Average Discount : {avg_discount}%\n")
    file.write(f"Average Opportunity Score : {avg_opportunity}\n\n")

    file.write("="*60 + "\n")
    file.write("Recommendation Distribution\n")
    file.write("="*60 + "\n")

    file.write(recommendations.to_string())

    file.write("\n\n")

    file.write("="*60 + "\n")
    file.write("Priority Distribution\n")
    file.write("="*60 + "\n")

    file.write(priority.to_string())

    file.write("\n\n")

    file.write("="*60 + "\n")
    file.write("Average Price by Platform\n")
    file.write("="*60 + "\n")

    file.write(platform.to_string())

    file.write("\n\n")

    file.write("="*60 + "\n")
    file.write("Top Brands by Opportunity Score\n")
    file.write("="*60 + "\n")

    file.write(brand.to_string())

    file.write("\n\n")

    file.write("="*60 + "\n")
    file.write("Top 10 Priority Products\n")
    file.write("="*60 + "\n")

    file.write(
        top_products[
            [
                "brand",
                "product_name",
                "priority_score",
                "priority",
                "final_recommendation"
            ]
        ].to_string(index=False)
    )

    file.write("\n\n")

    file.write("="*60 + "\n")
    file.write("Business Insights\n")
    file.write("="*60 + "\n\n")

    file.write(
        "- Products with high opportunity scores should receive immediate business attention.\n"
    )

    file.write(
        "- Premium products with excellent ratings can maintain higher pricing.\n"
    )

    file.write(
        "- Low-rated products require quality improvement before pricing changes.\n"
    )

    file.write(
        "- Promotional strategies should target products with medium opportunity scores.\n"
    )

    file.write(
        "- Priority products should be monitored daily for competitor price changes.\n"
    )

print("\nExecutive Summary Generated Successfully!")
print(f"Saved to: {EXECUTIVE_SUMMARY}")