import pandas as pd

print("Loading Master Dataset...")

df = pd.read_csv(
    "../data/master_product_dataset.csv"
)

print("\nInitial Records :", len(df))

# Remove duplicates
df.drop_duplicates(
    inplace=True
)

# Remove missing product names
df = df[
    df["product_name"].notna()
]

# Convert prices to numeric
df["current_price"] = pd.to_numeric(
    df["current_price"],
    errors="coerce"
)

df["original_price"] = pd.to_numeric(
    df["original_price"],
    errors="coerce"
)

# Convert ratings
df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)

# Convert review counts
df["review_count"] = pd.to_numeric(
    df["review_count"],
    errors="coerce"
)

# Fill missing values
df["rating"] = df["rating"].fillna(0)

df["review_count"] = df["review_count"].fillna(0)

print(
    "\nRecords After Cleaning :",
    len(df)
)

df.to_csv(
    "../data/cleaned_master_dataset.csv",
    index=False
)

print(
    "\nCleaned Dataset Saved Successfully"
)