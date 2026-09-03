print("S128 Aafiya Shaikh")

import pandas as pd

df = pd.read_csv("students - students.csv")

print("Marks in Ascending Order:")
print(df.sort_values("Marks"))

print("\nMarks in Descending Order:")
print(df.sort_values("Marks", ascending=False))

print("\nAttendance in Descending Order:")
print(df.sort_values("Attendance", ascending=False))

print("\nTop 5 Students:")
print(df.sort_values("Marks", ascending=False).head(5))

print("\nBottom 3 Students:")
print(df.sort_values("Marks").head(3))
