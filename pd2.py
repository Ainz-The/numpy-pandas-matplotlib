import pandas as pd
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
print(df['Age'].mean())
print(df['Fare'].max())
print(df['Fare'].min())
print(df['PassengerId'].count())

