import pandas as pd
import matplotlib.pyplot as plt

from config import *

print("Loading Dashboard Dataset...")

df = pd.read_csv("outputs/dashboard_dataset.csv")
plt.figure(figsize=(10,6))
df["final_recommendation"].value_counts().plot(kind="bar")

plt.title("Recommendation Distribution")
plt.xlabel("Recommendation")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/recommendation_distribution.png")
plt.close()


plt.figure(figsize=(10,6))
plt.hist(df["opportunity_score"],bins=10)
plt.title("Opportunity Score Distribution")
plt.xlabel("Opportunity Score")
plt.ylabel("Products")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/opportunity_score.png")
plt.close()


plt.figure(figsize=(8,6))
df["priority"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Priority Distribution")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/priority_distribution.png")
plt.close()



brand = df.groupby("brand")["opportunity_score"].mean()
brand = brand.sort_values(ascending=False)
plt.figure(figsize=(10,6))
brand.plot(kind="bar")
plt.title("Average Opportunity Score by Brand")
plt.xlabel("Brand")
plt.ylabel("Opportunity Score")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/brand_opportunity.png")
plt.close()


platform = df.groupby("platform")["current_price"].mean()
platform.plot(kind="bar",figsize=(8,6))
plt.title("Average Product Price by Platform")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/platform_analysis.png")
plt.close()


plt.figure(figsize=(8,6))
plt.scatter(df["current_price"],df["rating"])
plt.xlabel("Current Price")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/price_vs_rating.png")
plt.close()


plt.figure(figsize=(8,6))
plt.hist(df["discount_percent"],bins=10)
plt.title("Discount Distribution")
plt.xlabel("Discount %")
plt.ylabel("Products")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/discount_distribution.png")
plt.close()



top10 = df.sort_values(by="priority_score",ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.barh(top10["brand"],top10["priority_score"])
plt.title("Top Priority Products")
plt.xlabel("Priority Score")
plt.tight_layout()
plt.savefig(VISUAL_FOLDER + "/top_priority_products.png")
plt.close()

print()
print("====================================")
print("Visualization Completed Successfully")
print("====================================")
print()
print("Charts Saved In")
print("VISUAL_FOLDER")