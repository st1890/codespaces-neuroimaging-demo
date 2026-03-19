# Neuroimaging Mini Dataset (Codespaces Mini Repo)

A tiny repository for students to open in GitHub Codespaces and run a complete mini analysis.

## What is included

- `data/neuroimaging_demo.csv`: a small neuroimaging-style dataset (participants, motion, beta values, accuracy)
- `analyse.py`: a single analysis script using Pandas + Matplotlib
- `requirements.txt`: minimal dependencies

## Learning goal

Each student can create their own Codespace, run one script, and get:

- text summary statistics in the terminal
- a simple plot saved to `results/motion_vs_visual_beta.png`

## Run in Codespaces

1. Open the repository on GitHub.
2. Select **Code** > **Codespaces** > **Create codespace on main**.
3. In the Codespaces terminal, run:

```bash
python -m pip install -r requirements.txt
python analyse.py
```

## Typical extension tasks for students

- Add 5 new rows to the CSV with their own invented participants.
- Change the plot style or colours.
- Compute one extra summary (for example, baseline vs follow-up change by group).
- Save a cleaned CSV to `results/`.

## Notes for teaching

- This is intentionally small so setup is quick in class.
- Uses only simple tooling (`pip`) and standard data science libraries.
- Works well as a first Codespaces exercise before larger notebooks.
