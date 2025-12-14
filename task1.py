import pandas as pd

# 1. Load the CSV file
df = pd.read_csv("student_grades.csv")

# 2. Calculate each student's average score
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

# 3. Find the student with the highest average
top_student = df.loc[df["Average"].idxmax()]

# 4. Print the full DataFrame
print("=== Student Grades with Averages ===")
print(df)
print()

# 5. Print the top student
print("=== Student with Highest Average ===")
print(f"Name: {top_student['Name']}")
print(f"Math: {top_student['Math']}")
print(f"English: {top_student['English']}")
print(f"Science: {top_student['Science']}")
print(f"Average Score: {top_student['Average']:.2f}")
