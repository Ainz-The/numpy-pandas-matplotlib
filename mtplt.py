import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\zaink\Downloads\titanic.csv")
class_count = df['Pclass'].value_counts().sort_index()
plt.bar(class_count.index, class_count.values)
plt.xlabel("Passenger Class")
plt.ylabel("Passenger Count")
plt.title("Passenger Count by Class")
plt.show()
