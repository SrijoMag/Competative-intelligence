import pandas as pd

print("Loading CSV Files...")

croma_df = pd.read_csv(
    "../data/croma_products_day3.csv"
)

flipkart_df = pd.read_csv(
    "../data/flipkart_products_day3_new.csv"
)

amazon_df = pd.read_csv(
    "../data/amazon_products_day3.csv"
)

print("Merging Datasets...")

master_df = pd.concat(
    [
        croma_df,
        flipkart_df,
        amazon_df
    ],
    ignore_index=True
)

master_df.drop_duplicates(
    inplace=True
)
required_cols = [
    "timestamp",
    "platform",
    "brand",
    "product_name",
    "current_price",
    "original_price",
    "discount_percent",
    "rating",
    "review_count",
    "url"
]

for col in required_cols:
    if col not in master_df.columns:
        master_df[col] = None

master_df = master_df[required_cols]
master_df.to_csv(
    "../data/master_product_dataset.csv",
    index=False
)

print("\nMaster Dataset Created Successfully")

print(
    "\nTotal Records :",
    len(master_df)
)

print(
    "\nColumns :"
)

print(
    master_df.columns.tolist()
)

print(
    "\nSaved As : master_product_dataset.csv"
)