import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
plt.hist(df['Age'].dropna(), bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Age Distribution of Passengers")
plt.show()