import pandas as pd

df=pd.read_csv("data/master_product_dataset.csv")
print("Original Sgape:",df.shape)
df=df.drop_duplicates()

df['brand'] = df['brand'].astype(str).str.title()
df['rating'] = (
    df['rating']
    .astype(str)
    .str.extract(r'(\d+\.?\d*)')[0]
)

df['rating'] = pd.to_numeric(
    df['rating'],
    errors='coerce'
)

df['review_count'] = (
    df['review_count']
    .astype(str)
    .str.replace(',', '', regex=False)
)

df['review_count'] = pd.to_numeric(
    df['review_count'],
    errors='coerce'
)

price_cols = [
    'current_price',
    'original_price',
    'discount_percent'
]

for col in price_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.replace('₹', '', regex=False)
    )
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

df['rating'] = df['rating'].fillna(
    df['rating'].median()
)
df['review_count'] = df['review_count'].fillna(0)
df['discount_percent'] = df['discount_percent'].fillna(0)
df['original_price'] = df['original_price'].fillna(
    df['current_price']
)

df = df.dropna(subset=['current_price'])
print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/cleaned_dataset.csv",
    index=False
)
print("Data Cleaning Completed Successfully")