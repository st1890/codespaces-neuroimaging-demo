from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    project_root = Path(__file__).parent
    data_path = project_root / "data" / "neuroimaging_demo.csv"
    output_dir = project_root / "results"
    output_dir.mkdir(exist_ok=True)

    df = pd.read_csv(data_path)

    print("Mini Neuroimaging Dataset")
    print("-" * 24)
    print(f"Rows: {len(df)}")
    print(f"Columns: {', '.join(df.columns)}")
    print()

    mean_fd = df["MeanFD_mm"].mean()
    mean_acc = df["AccuracyPct"].mean()

    print(f"Average head motion (Mean FD): {mean_fd:.3f} mm")
    print(f"Average task accuracy: {mean_acc:.1f}%")
    print()

    by_group = (
        df.groupby("Group", as_index=False)
        .agg(
            avg_motion_mm=("MeanFD_mm", "mean"),
            avg_motor_beta=("MotorBeta", "mean"),
            avg_visual_beta=("VisualBeta", "mean"),
            avg_accuracy=("AccuracyPct", "mean"),
            n=("ParticipantID", "count"),
        )
        .sort_values("avg_accuracy", ascending=False)
    )

    print("Group summary")
    print(by_group.to_string(index=False, float_format=lambda x: f"{x:.3f}"))

    fig, ax = plt.subplots(figsize=(7, 5))
    colour_map = {"Control": "steelblue", "Patient": "tomato"}

    for group, group_df in df.groupby("Group"):
        group_name = str(group)
        ax.scatter(
            group_df["MeanFD_mm"],
            group_df["VisualBeta"],
            s=80,
            alpha=0.85,
            label=group_name,
            color=colour_map.get(group_name, "grey"),
        )

    for _, row in df.iterrows():
        ax.annotate(
            row["ParticipantID"],
            (row["MeanFD_mm"], row["VisualBeta"]),
            textcoords="offset points",
            xytext=(4, 4),
            fontsize=8,
        )

    ax.set_title("Head Motion vs Visual Activation")
    ax.set_xlabel("Mean FD (mm)")
    ax.set_ylabel("Visual Beta")
    ax.legend(title="Group")
    fig.tight_layout()

    output_plot = output_dir / "motion_vs_visual_beta.png"
    fig.savefig(str(output_plot), dpi=150)
    print()
    print(f"Saved plot: {output_plot}")


if __name__ == "__main__":
    main()
