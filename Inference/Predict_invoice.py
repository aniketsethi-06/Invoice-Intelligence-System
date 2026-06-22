import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "predict_flag_invoice1.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler1.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def load_scaler():
    return joblib.load(SCALER_PATH)


def predict_invoice_flag(input_data):

    model = load_model()
    scaler = load_scaler()

    input_df = pd.DataFrame(input_data)
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    input_df["Predicted_Flag"] = prediction
    input_df["High_Risk_Probability"] = probability[:, 1]

    return input_df


if __name__ == "__main__":

    sample_data = {
        "invoice_quantity": [1000],
        "invoice_dollars": [2000],
        "Freight": [200],
        "total_item_quantity": [1000],
        "total_item_dollars": [2020]
    }

    prediction = predict_invoice_flag(sample_data)

    print(prediction)