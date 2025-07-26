import streamlit as st
from predictor import predict_churn

st.set_page_config(page_title="Churn Predictor", page_icon="📊")

st.title("Customer Churn Prediction App")
st.markdown("Enter just three fields below to predict whether a customer will churn.")

# 🧾 Input Fields
tenure = st.slider("Tenure (in months)", 0, 72, 24)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])


payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

# Smart logic for grouping
contract_type = "Short-Term" if contract == "Month-to-month" else "Long-Term"

tenure_group = (
    "0-12" if tenure <= 12 else
    "13-24" if tenure <= 24 else
    "25-36" if tenure <= 36 else
    "37-48" if tenure <= 48 else
    "49-60" if tenure <= 60 else "61-72"
)

InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

# Build input with default values
user_input = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "No",
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": contract,
    "PaperlessBilling": "Yes",
    "PaymentMethod": payment_method,
    "contract_type": contract_type,
    "tenure_group": tenure_group,
    "tenure": tenure,
    "MonthlyCharges": 70.0  # Avg value or default
}

if st.button("🚀 Predict Churn"):
    pred, prob = predict_churn(user_input)

    st.markdown("---")
    if pred == 1:
        st.error(f"⚠️ Likely to Churn\n\n**Probability:** {prob:.2%}")
    else:
        st.success(f"✅ Likely to Stay\n\n**Churn Probability:** {prob:.2%}")