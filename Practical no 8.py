print("S128 Aafiya Shaikh") 

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.title("Restaurant Bill vs Tip")
plt.show()
