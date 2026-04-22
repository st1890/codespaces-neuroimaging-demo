# Neuroimaging Teaching Demo

This is a small beginner-friendly project for practicing simple data analysis in Python.

## What this script does

The script in `analyse.py`:

1. Loads a CSV file of demo neuroimaging-style participant data.
2. Prints basic dataset info (rows and column names).
3. Calculates overall averages for:
	- head motion (`MeanFD_mm`)
	- task accuracy (`AccuracyPct`)
4. Prints a group summary table (`Control` vs `Patient`).

## Project files

- `data/neuroimaging_demo.csv`: input dataset
- `analyse.py`: analysis script
- `requirements.txt`: Python packages to install

## Quick start
You can run the original script 'as is' - the two libraries it needs (Pandas, Numpy) are available in the default installation.

Once you start adding to the project, you will need some additional libraries. Often
you will find that repositories on GitHub come with a list of modules that you need
in a file called 'requirements.txt'. You can install all these modules in one go like this:


Run these commands in the terminal:

```bash
pip install -r requirements.txt
```

## What output should look like

You should see:

- a title: `Mini Neuroimaging Dataset`
- row count and column names
- average motion and accuracy
- a small group summary table

## Beginner exercises

1. Add 2-5 new participants to `data/neuroimaging_demo.csv`.
2. Re-run the script and compare how averages change.
3. Add one new summary metric to `analyse.py`.

## If something fails

- If `pip` is not found, try: `python -m pip install -r requirements.txt`
- If imports fail, re-run the install command.
