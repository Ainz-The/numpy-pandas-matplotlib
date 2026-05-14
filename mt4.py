import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
plt.scatter(df['Age'], df['Fare'])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare")
plt.show()