import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
gender_count = df['Sex'].value_counts()
plt.pie(gender_count.values, labels=gender_count.index,autopct='%1.1f%%')
plt.title("Male vs Female Passengers")
plt.show()