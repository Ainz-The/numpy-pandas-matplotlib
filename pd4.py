import pandas as pd
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df['Age'].isnull().sum())
df = df.dropna(subset=['Embarked'])
print(df['Embarked'].isnull().sum())