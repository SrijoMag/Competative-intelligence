import pandas as pd
df=pd.read_csv(r"C:\Users\KIIT0001\Desktop\Project\week5\week3\data\pricing_recommendations.csv")
df["aggressive_price"]=(df["current_price"]*0.95)
df["conservative_price"]=(df["current_price"]*0.98)

print(
    df[
        [
            "product_name",
            "current_price",
            "aggressive_price",
            "conservative_price"
        ]
    ].head()
)