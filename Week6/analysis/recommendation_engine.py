
import pandas as pd
import numpy as np

from config import *

print("Loading datasets...")
df = pd.read_csv("..\week5\data\pricing_recommendations.csv")
print("Total Products :", len(df))

df["current_price"] = pd.to_numeric(df["current_price"], errors="coerce")
df["discount_percent"] = pd.to_numeric(df["discount_percent"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce")

df.fillna(0, inplace=True)

def business_rule(row):

    price = row["current_price"]
    rating = row["rating"]
    discount = row["discount_percent"]
    reviews = row["review_count"]

    if price >= HIGH_PRICE and rating >= GOOD_RATING:
        return "Premium Positioning"

    elif price >= HIGH_PRICE and rating < AVERAGE_RATING:
        return "Reduce Price"

    elif discount >= 70:
        return "Maintain Price"

    elif discount >= 40:
        return "Increase Promotion"

    elif price <= LOW_PRICE and reviews >= HIGH_REVIEWS:
        return "Bundle Offer"

    elif rating < 3.5:
        return "Improve Product Quality"

    elif MID_PRICE <= price <= HIGH_PRICE:
        return "Monitor Competitor"

    else:
        return "Maintain Price"


print("Generating Business Recommendations...")

df["business_recommendation"] = df.apply(
    business_rule,
    axis=1
)

def decision_tree(row):

    price = row["current_price"]
    rating = row["rating"]
    discount = row["discount_percent"]

    if rating < 3.5:

        if price > 5000:
            return "Reduce Price"

        else:
            return "Improve Features"

    else:

        if discount > 60:
            return "Maintain"

        elif discount > 30:
            return "Promotion"

        elif price > 7000:
            return "Premium"

        else:
            return "Stable"

print("Building Decision Tree...")

df["decision"] = df.apply(
    decision_tree,
    axis=1
)

print("Calculating Opportunity Score...")
price_score = (1-(df["current_price"] /df["current_price"].max()))

rating_score = (df["rating"] /5)
discount_score = (df["discount_percent"] /100)
review_score = (df["review_count"]
                 /(df["review_count"].max()
                   if df["review_count"].max() != 0     
                   else 1
    )
)

df["opportunity_score"] = (

    PRICE_WEIGHT * price_score +

    RATING_WEIGHT * rating_score +

    DISCOUNT_WEIGHT * discount_score +

    REVIEW_WEIGHT * review_score

) * MAX_SCORE

df["opportunity_score"] = df["opportunity_score"].round(2)

def opportunity_level(score):

    if score >= 80:
        return "Excellent"

    elif score >= 65:
        return "High"

    elif score >= 50:
        return "Medium"

    else:
        return "Low"

df["opportunity_level"] = df["opportunity_score"].apply(opportunity_level)
print("Calculating Priority Score...")

priority = (df["opportunity_score"]+df["rating"] * 5 +df["discount_percent"] * 0.2)
df["priority_score"] = priority.round(2)

def priority(row):

    score = row["priority_score"]

    if score >= 100:
        return "Critical"

    elif score >= 80:
        return "High"

    elif score >= 60:
        return "Medium"

    else:
        return "Low"

df["priority"] = df.apply(
    priority,
    axis=1
)

print("Applying Business Constraints...")

def constraints(row):

    action = row["business_recommendation"]

    price = row["current_price"]

    if action == "Reduce Price":

        if price < 1000:
            return "Maintain Price"

    if action == "Premium Positioning":

        if row["rating"] < 4:
            return "Maintain Price"

    return action

df["final_recommendation"] = df.apply(constraints,axis=1)
df = df.sort_values(by="priority_score",ascending=False)
df["rank"] = range(1,len(df) + 1)

print("Saving Outputs...")

df.to_csv(STRATEGIC_RECOMMENDATION,index=False)

df[
    [
        "brand",
        "product_name",
        "opportunity_score",
        "opportunity_level"
    ]
].to_csv(
    OPPORTUNITY_SCORE,
    index=False
)

df[
    [
        "brand",
        "product_name",
        "priority_score",
        "priority",
        "rank"
    ]
].to_csv(
    PRIORITY_PRODUCTS,
    index=False
)

df.to_csv(DASHBOARD_DATASET,index=False)

print()

print("=====================================")
print("Week 6 Recommendation Engine Completed")
print("=====================================")

print()

print("Generated Files")

print("Strategic Recommendations")

print("Opportunity Scores")

print("Priority Products")

print("Dashboard Dataset")

print()

print("Top 10 Products")

print(
    df[
        [
            "brand",
            "product_name",
            "priority_score",
            "priority"
        ]
    ].head(10)
)