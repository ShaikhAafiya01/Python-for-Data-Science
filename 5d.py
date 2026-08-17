print("S128 Aafiya Shaikh")

import pandas as pd

marks = pd.Series([45, 67, 89, 32, 90, 76])

filtered = marks[marks > 60]

print(filtered) 
