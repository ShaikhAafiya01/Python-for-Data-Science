print("S128 Aafiya Shaikh")

import pandas as pd

df = pd.read_csv("students - students.csv")

print("Number of Students in Each Course:")
print(df.groupby("Course")["Name"].count())

print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nMaximum Marks by Course:")
print(df.groupby("Course")["Marks"].max())

print("\nAverage Attendance by Course:")
print(df.groupby("Course")["Attendance"].mean())
