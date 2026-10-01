import os
import numpy as np
import pandas as pd

def clean_data(
    input_path="data/raw/diabetic_data.csv",
    output_path="data/cleaned_step1.csv"
):
    print("--- Starting Data Cleaning & Deduplication ---")
    df = pd.read_csv(input_path)
    print(f"Initial shape: {df.shape}")

    # 1. Standardize missing indicators
    df.replace("?", np.nan, inplace=True)

    # 2. Drop identical duplicate rows
    df.drop_duplicates(inplace=True)

    # 3. Patient-level deduplication: retain initial encounter only
    if "patient_nbr" in df.columns and "encounter_id" in df.columns:
        df.sort_values(by="encounter_id", inplace=True)
        df.drop_duplicates(subset=["patient_nbr"], keep="first", inplace=True)

    # 4. Filter terminal discharge dispositions
    if "discharge_disposition_id" in df.columns:
        terminal_ids = [11, 13, 14, 19, 20, 21]
        df = df[~df["discharge_disposition_id"].isin(terminal_ids)]

    # 5. Remove IDs and sparse columns
    drop_cols = ["encounter_id", "patient_nbr", "weight", "payer_code", "medical_specialty"]
    df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)

    # 6. Save intermediate cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data successfully saved to: {output_path}")
    print(f"Final cleaned shape: {df.shape}")

if __name__ == "__main__":
    clean_data()
