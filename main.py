import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    initial_rows = len(df)
    print(f"Starting cleaning. Initial rows: {initial_rows}")

    if 'name' in df.columns:
        df['name'] = df['name'].str.strip().str.title()
    
    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.strip().str.capitalize()

    numeric_cols = ["age", "salary"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        mean_val = df[col].mean()
        df[col] = df[col].fillna(mean_val)

    df["age"] = df["age"].round().astype(int)

    df = df.dropna(subset=["name"])

    df = df.drop_duplicates(subset=["name", "age"])

    df["gender"] = df["gender"].fillna("Unknown")

    final_rows = len(df)
    print(f"Cleaning complete.")
    print(f"Rows removed: {initial_rows - final_rows}")
    print(f"Final row count: {final_rows}")

    df.to_csv(output_path, index=False)

def main():
    input_file = "data/raw_data.csv"
    output_file = "data/cleaned_data.csv"

    success = clean_data(input_file, output_file)
    
    if success:
        print("\nPipeline executed successfully! ✅")
    else:
        print("\nPipeline failed. ❌")
        
if __name__ == "__main__":
    clean_data("data/raw_data.csv", "data/cleaned_data.csv")