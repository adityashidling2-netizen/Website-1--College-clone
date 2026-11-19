import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load data
data = sns.load_dataset('titanic')
print(data.head)

#bar plot
plt.bar(data['alive'], data['age'])
plt.title("Bar plot for visualization")
plt.xlabel("Alive people")
plt.ylabel("Age of people")
plt.show()

#histogram
plt.hist(data['age'], bins=5)
plt.title("Histogram for visualization")
plt.xlabel("Age of people")
plt.ylabel("Level of ages")
plt.show()

a = data['class'].value_counts()
a.plot(kind='line')
plt.title("Line plot for visualization")
plt.xlabel("class of people")
plt.ylabel("Passengers")
plt.show()

#pie char
plt.pie(data['class'].value_counts(), labels=[1,2,3], autopct='%1.2f%%')
plt.show()

#scatter plot
plt.scatter(data["age"], data['fare'])
plt.title("Scatter plot for visualization")
plt.xlabel("Age of people")
plt.ylabel("Fare of titanic")
plt.show()

#box plot
data['age'].plot(kind='box')
plt.title("Box plot for visaulization")
plt.ylabel("fare")
plt.show()