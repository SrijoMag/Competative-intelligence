import pandas as pd
df=pd.read_csv(r"C:\Users\KIIT0001\Desktop\Project\week5\week3\data\pricing_recommendations.csv")
high_priority=df[df["recommendation"]=="Reduse Price"]
print("\n=====ALERTS====\n")

for product in high_priority["product_name"]:
    print(f"PRICE ACTION REQUIRED: {product}")