import pandas as pd
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
print(df[df['Age']>30])
print(df[df['Sex']=='female'])
print(df[df['Survived']==1])
print(df[df['Pclass']==1])


