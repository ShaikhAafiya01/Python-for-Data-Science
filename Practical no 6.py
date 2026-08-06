print("S128 Aafiya Shaikh")

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.show()

plt.figure()
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Customized Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")
plt.show()

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [85, 70, 74, 60]

plt.figure()
plt.bar(categories, scores)
plt.title("Student Scores")
plt.show()

plt.figure()
plt.barh(categories, scores)
plt.title("Student Scores")
plt.show()

explode = [0, 0, 0, 0.1]

plt.figure()
plt.pie(scores, labels=categories, autopct="%1.1f%%", explode=explode)
plt.show()

x1 = [5, 7, 8, 7, 6, 9, 5]
y1 = [99, 86, 87, 88, 100, 86, 103]

plt.figure()
plt.scatter(x1, y1, color="green", s=100)
plt.show()

data = np.random.normal(0, 1, 100)

plt.figure()
plt.hist(data, bins=20)
plt.grid(True)
plt.show()

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, y)
ax[0, 0].set_title("Line Plot")

ax[0, 1].bar(categories, scores)
ax[0, 1].set_title("Bar Chart")

ax[1, 0].scatter(x1, y1)
ax[1, 0].set_title("Scatter Plot")

ax[1, 1].hist(data, bins=20)
ax[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

plt.figure()
plt.plot(months, sales_2023, "b--o", label="2023")
plt.plot(months, sales_2024, "g-s", label="2024")

m = max(sales_2024)
i = sales_2024.index(m)

plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

plt.annotate("Highest", (months[i], m), (months[i], m + 30),
             arrowprops=dict(arrowstyle="->"))

plt.savefig("sales_comparison.png")
plt.show()
