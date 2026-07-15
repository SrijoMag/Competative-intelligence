import pandas as pd
df=pd.read_csv("data/normalized_dataset.csv")
scorecard=pd.DataFrame()
scorecard['Column']=df.columns
scorecard['Missing Values']=df.isnull().sum().values
scorecard['Completeness %']=((1-df.isnull().mean())*100).values

scorecard.to_csv("data/quality_scoreboard.csv",index=False)
print(scorecard)