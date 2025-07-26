import pandas as pd
import joblib

# Load model and reference column list
model = joblib.load('C:\customer-churn-project\model\hybrid_model.pk1')

# This is your final list of columns after get_dummies during training
# Save it from your training notebook using: `joblib.dump(X.columns.tolist(), 'model/columns.pkl')`
expected_columns = joblib.load('C:/customer-churn-project/model/columns.pkl')  

# List of categorical columns used for encoding
categorical_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                    'PhoneService', 'MultipleLines', 'InternetService',
                    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies',
                    'Contract', 'PaperlessBilling', 'PaymentMethod',
                    'contract_type', 'tenure_group']

def predict_churn(input_data : dict):
    df = pd.DataFrame([input_data])

    # One-hot encode with same logic as training
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Align the new data with expected columns
    df_encoded = df_encoded.reindex(columns=expected_columns, fill_value=0)

    # Predict
    prediction = model.predict(df_encoded)[0]
    probability = model.predict_proba(df_encoded)[0][1]

    return prediction, probability
