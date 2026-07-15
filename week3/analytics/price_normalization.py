import pandas as pd

df=pd.read_csv("data/cleaned_dataset.csv")

df['Effective+price']=df['current_price']
df['price_difference']=(df['original_price']-df['current_price'])
df['saving percentage']=(df['price_difference']/df['original_price'])*100
df.to_csv("data/normalized_dataset.csv",index=False)
print("Price Normalization Complite")