import pandas as pd
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
print(df.head(5))
print(df.shape)
print(df.columns)
print(df.info())
