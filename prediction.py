# inference.py

import joblib
import pandas as pd

def run_inference():
    # === 1. Load Model ===
    model = joblib.load("model.pkl")  # Ganti dengan nama file model kamu
    print("✅ Model berhasil dimuat.")

    # === 2. Load Data Testing ===
    X_test = pd.read_csv("X_test.csv")  # Pastikan kamu simpan X_test ke file ini
    y_test = pd.read_csv("y_test.csv")  # Label asli untuk evaluasi opsional

    # === 3. Prediksi ===
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # === 4. Gabungkan hasil ke DataFrame ===
    df_result = X_test.copy()
    df_result['Attrition_Prob'] = y_prob
    df_result['Attrition_Predicted'] = y_pred
    df_result['Attrition_True'] = y_test.values

    # === 5. Simpan Hasil ===
    df_result.to_csv("hasil_inference.csv", index=False)
    print("📁 Hasil inference disimpan ke hasil_inference.csv")

if __name__ == "__main__":
    run_inference()
