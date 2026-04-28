"""
This script performs a tiny end-to-end analysis of a neuroimaging demo dataset.
Here we are interested in two behavioural things that might affect the quality of our fMRI data:
1. Head motion (MeanFD_mm) - more motion can degrade data quality.
2. Task accuracy (AccuracyPct) - lower accuracy might indicate less engagement with the task.
What it does:
1. Loads the CSV file from the data folder.
2. Prints basic dataset information (row count and column names).
3. Computes overall averages for head motion and task accuracy.
4. Computes per-group summaries (Control vs Patient) for key metrics.
5. Prints the group summary table, sorted by highest average accuracy.

The goal is to show a complete beginner-friendly analysis workflow in one file.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This script is intentionally written as a simple top-level script (no main function)
# so new learners can read it from top to bottom in execution order.

# Build a path to the folder where this script lives.
# Using Path(__file__) makes the script work no matter where you run it from.
project_root = Path(__file__).parent

# Build the full path to the CSV file we want to analyse.
data_path = project_root / "data" / "neuroimaging_demo.csv"

# Read the CSV into a Pandas DataFrame.
# A DataFrame is a table-like object (rows + columns), similar to a spreadsheet.
df = pd.read_csv(data_path)

# Print a simple title section in the terminal.
print("Mini Neuroimaging Dataset")
print("-" * 24)

# Show basic dataset shape information.
print(f"Rows: {len(df)}")

# df.columns contains the column names; join them into one readable line.
print(f"Columns: {', '.join(df.columns)}")
print()

# Calculate overall averages across all participants.
# np.mean returns the arithmetic mean of each selected numeric column.
mean_fd = np.mean(df["MeanFD_mm"])
mean_acc = np.mean(df["AccuracyPct"])

# Print overall summary values with formatting:
# - {mean_fd:.3f} means 3 decimal places
# - {mean_acc:.1f} means 1 decimal place
print(f"Average head motion (Mean FD): {mean_fd:.3f} mm")
print(f"Average task accuracy: {mean_acc:.1f}%")
print()

print("Group summary")

# Group rows by the Group column (for example Control vs Patient),
# then compute one set of summary statistics for each group.
#
# agg(...) defines output columns:
# - N: number of participants
# - AvgMotion: average MeanFD_mm
# - AvgMotor: average MotorBeta
# - AvgVisual: average VisualBeta
# - AvgAccuracy: average AccuracyPct
group_summary = df.groupby("Group").agg(
    N=("ParticipantID", "count"),
    AvgMotion=("MeanFD_mm", "mean"),
    AvgMotor=("MotorBeta", "mean"),
    AvgVisual=("VisualBeta", "mean"),
    AvgAccuracy=("AccuracyPct", "mean"),
    MedianAccuracy=("AccuracyPct","median")

)

# Sort groups so highest accuracy appears first, then round values
# to make the printed table easier to read in class.
print(group_summary.sort_values("AvgAccuracy", ascending=False).round(3))

# Create one boxplot per numeric column so each measure can be inspected individually.
numeric_cols = df.select_dtypes(include="number").columns

# Use a polished seaborn style and a soft color palette.
sns.set_theme(style="whitegrid", context="talk")
palette = sns.color_palette("Set2", len(numeric_cols))

# Arrange plots in two columns for better visual balance.
n_cols = 2
n_rows = int(np.ceil(len(numeric_cols) / n_cols))
fig, axes = plt.subplots(
    n_rows,
    n_cols,
    figsize=(14, 4.5 * n_rows),
    facecolor="#f7f7f7",
)

axes = np.array(axes).reshape(-1)

for i, (ax, col) in enumerate(zip(axes, numeric_cols)):
    values = df[col].dropna()
    color = palette[i]

    sns.boxplot(
        y=values,
        ax=ax,
        color=color,
        width=0.4,
        saturation=0.9,
        fliersize=4,
        linewidth=1.6,
        boxprops={"alpha": 0.85},
        medianprops={"color": "#222222", "linewidth": 2.2},
        whiskerprops={"linewidth": 1.6},
        capprops={"linewidth": 1.6},
    )

    # Overlay points so viewers can see sample spread and potential clusters.
    sns.stripplot(
        y=values,
        ax=ax,
        color="#2f2f2f",
        size=4,
        alpha=0.55,
        jitter=0.18,
    )

    ax.set_title(f"{col}", fontsize=13, pad=10, weight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Value", fontsize=11)
    ax.set_facecolor("#ffffff")
    ax.grid(True, axis="y", alpha=0.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Hide any unused axes when the number of columns is odd.
for ax in axes[len(numeric_cols):]:
    ax.axis("off")

fig.suptitle(
    "Distributions Across Individual Numeric Columns",
    y=1.01,
    fontsize=18,
    weight="bold",
)
fig.tight_layout(pad=1.2)
fig.savefig(project_root / "individual_column_boxplots.png", dpi=150)
plt.show()

