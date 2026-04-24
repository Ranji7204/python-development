import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# 1. Load Data
# ================================
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

# ================================
# 2. Basic Analysis
# ================================
print("\nSummary statistics:")
print(df.describe())

# Example: Average of a column
column_name = df.columns[1]  # change if needed
avg = df[column_name].mean()
print(f"\nAverage of {column_name}: {avg}")

# ================================
# 3. Visualization
# ================================

# Bar Chart
df[column_name].value_counts().head(10).plot(kind='bar')
plt.title("Bar Chart")
plt.savefig("fig1_bar.png")
plt.clf()

# Scatter Plot
if len(df.columns) >= 2:
    plt.scatter(df[df.columns[0]], df[df.columns[1]])
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title("Scatter Plot")
    plt.savefig("fig2_scatter.png")
    plt.clf()

# Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Heatmap")
plt.savefig("fig3_heatmap.png")
plt.clf()

# ================================
# 4. Insights
# ================================
print("\nInsights:")
print("- Check correlation from heatmap.")
print("- Identify trends from scatter plot.")
print("- Distribution seen in bar chart.")
