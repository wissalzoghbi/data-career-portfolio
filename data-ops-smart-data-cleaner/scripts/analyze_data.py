import pandas as pd
import os

def get_cleaning_suggestions(df):
    suggestions = []
    
    # 1. Suggest dropping columns with more than 50% null values
    for column in df.columns:
        null_ratio = df[column].isnull().mean()
        if null_ratio > 0.5:
            suggestions.append(f"Consider dropping column '{column}' (more than 50% missing values).")
    
    # 2. Suggest filling missing values
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            if df[column].dtype == 'object':
                suggestions.append(f"Column '{column}' has missing values. Fill with the most frequent value (mode).")
            else:
                suggestions.append(f"Column '{column}' has missing values. Fill with mean or median.")
    
    # 3. Suggest type conversions
    for column in df.select_dtypes(include='object').columns:
        try:
            pd.to_numeric(df[column])
            suggestions.append(f"Column '{column}' could be converted to numeric.")
        except:
            continue

    return suggestions

def analyze_data(df):
    try:
        # 1. Generate statistical summary
        description = df.describe(include='all')
        print("=== Description ===")
        print(description)

        # 2. Check null values
        nulls = df.isnull().sum()
        print("\n=== Null Values ===")
        print(nulls)

        # 3. Get cleaning suggestions
        suggestions = get_cleaning_suggestions(df)
        print("\n=== Cleaning Suggestions ===")
        for s in suggestions:
            print("-", s)

        # 4. Save report to file
        report_path = "outputs/report.txt"
        f = open(report_path, "w", encoding="utf-8")

        f.write("=== Description ===\n")
        f.write(description.to_string())
        f.write("\n\n=== Null Values ===\n")
        f.write(nulls.to_string())
        f.write("\n\n=== Cleaning Suggestions ===\n")
        for s in suggestions:
            f.write(f"- {s}\n")

        f.close()
        print(f"\n✅ Report saved to: {report_path}")

    except Exception as e:
        print(f"Could not analyze data: {e}")



   

if __name__ == "__main__":
    try:
        # Load CSV
        data_path = os.path.join("data", "ames.csv")  # Or your dataset
        df = pd.read_csv(data_path)
        analyze_data(df)
    except Exception as e:
        print(f"Could not analyze data: {e}")