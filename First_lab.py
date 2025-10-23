import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv("Titanic-Dataset.csv")

#plt.figure(figsize=(10,6))
#sb.histplot(data=df,x='Fare',bins=50,kde=True,color='skyblue')
#plt.title("Distribution of Fare prices")
#plt.xlabel("Fare")
#plt.ylabel("Frequency")
#plt.show()

plt.figure(figsize=(12,8))
sb.barplot(x='Pclass',y='Fare',data=df)
plt.title('Tickey fare by class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

#plt.title("Relationship between class and fare")
#plt.xlabel("Class")
#plt.ylabel("Fare")
#plt.show()