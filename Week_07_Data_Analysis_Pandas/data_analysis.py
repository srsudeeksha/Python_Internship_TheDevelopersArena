# week7_data_analysis.py

import pandas as pd

def load_data(filename):
    """Load the CSV file and return a DataFrame."""
    try:
        df = pd.read_csv(filename)
        print(f"✅ Successfully loaded '{filename}'\n")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        exit()

def display_head(df, rows=5):
    """Display the first few rows of the dataset."""
    print("📌 First rows of the dataset:")
    print(df.head(rows))
    print("\n" + "-" * 50 + "\n")

def display_info(df):
    """Display dataset info."""
    print("📌 Dataset Info:")
    print(df.info())
    print("\n" + "-" * 50 + "\n")

def display_statistics(df):
    """Display summary statistics of numeric columns."""
    print("📌 Summary Statistics:")
    print(df.describe())
    print("\n" + "-" * 50 + "\n")

def average_score_by_subject(df):
    """Display average score for each subject."""
    print("📌 Average Score by Subject:")
    print(df.groupby("Subject")["Score"].mean())
    print("\n" + "-" * 50 + "\n")

def main():
    filename = "student_scores.csv"
    df = load_data(filename)

    display_head(df)
    display_info(df)
    display_statistics(df)
    average_score_by_subject(df)

if __name__ == "__main__":
    main()
