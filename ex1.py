import numpy as np
import pandas as pd

# Creating employee data using NumPy
data = np.array([
    [101, "Arun", "Developer", 2, 25, 8000],
    [102, "Bala", np.nan, 5, 30, 12000],
    [103, "Charan", "Analyst", 3, 28, 9500],
    [104, "Divya", "Manager", 8, 40, 15000],
    [105, "Esha", np.nan, 1, 22, 7000]
])

# Creating DataFrame
columns = ["empid", "name", "designation", "years_of_experience", "age", "salary"]
df = pd.DataFrame(data, columns=columns)

print("Original DataFrame:\n")
print(df)

# Convert numeric columns properly
df["years_of_experience"] = df["years_of_experience"].astype(int)
df["age"] = df["age"].astype(int)
df["salary"] = df["salary"].astype(int)

# 1) Increment age by 3
df["age"] = df["age"] + 3

# 2) Rename years_of_experience to exp
df.rename(columns={"years_of_experience": "exp"}, inplace=True)

# 3) Drop rows where salary > 10000
df = df[df["salary"] <= 10000]

# 4) Handle NA values in designation (fill with "Not Assigned")
df["designation"].fillna("Not Assigned", inplace=True)

print("\nUpdated DataFrame:\n")
print(df)