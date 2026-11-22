import pandas as pd

data = {
    "Name": ["Arun", "Kumar", "Ravi", "Vijay"],
    "Marks": [85, 90, 75, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())
