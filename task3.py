import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("satisfactionreport.csv")

# Count satisfaction levels
satisfaction_counts = df["Satisfaction_Level"].value_counts()

# Print counts
print(satisfaction_counts)

# Plot bar chart
plt.figure()
satisfaction_counts.plot(kind='bar')

# Labels and title
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of Employees")
plt.title("Employee Satisfaction Survey Results")

# Show chart
plt.show()
