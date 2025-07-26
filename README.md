📊 Customer Churn Prediction: End-to-End Data Science Project

A complete machine learning pipeline to predict customer churn, combining technical accuracy and business insight. This project covers data preparation, modeling, evaluation, deployment, and dashboarding.

🔍 Project Goal

Predict whether a customer will churn (leave) using historical data, then present predictions and insights using:

A machine learning model with custom threshold tuning

A Streamlit app for prediction

A Power BI dashboard for insights

🔧 Tech Stack

Languages: Python, SQL

Libraries: Pandas, Scikit-learn, XGBoost, imbalanced-learn, joblib, matplotlib, seaborn

App & Visualization: Streamlit, Power BI

📂 Folder Structure
```bash
  customer-churn-project/
  ├── data/                     # Cleaned + expanded dataset
  ├── model/                    # Trained model + feature columns
  ├── app/                      # Streamlit frontend/backend
  ├── notebooks/                # EDA and model building notebook
  ├── powerbi/                # Power BI file
  ├── requirements.txt
  ├── README.md

```
👄 1. Data Collection

Used IBM's Telco Customer Churn dataset (originally ~7000 rows)

Used data augmentation to expand it to ~30,000 rows with meaningful churn patterns

```
import pandas as pd
import numpy as np

# Load original data
original_df = pd.read_csv('data/customer_churn.csv')
```
DATA:
![Snap_1](https://i.postimg.cc/y62yvPTY/Data.png)

![Snap_6](https://i.postimg.cc/XJQDrCMB/Churn-Distribution.png)

![Snap_2](https://i.postimg.cc/2yHRNtjJ/Tenure-Vs-Churn.png)

![Snap_3](https://i.postimg.cc/MHpN5Y0Y/Churn-By-Contract.png)

![Snap_4](https://i.postimg.cc/pXy3nqLW/Churn-By-Payment-method.png)

![Snap_5](https://i.postimg.cc/4x9MWycj/Monthly-Vs-Churn.png)


🔄 2. Feature Engineering

Converted categorical variables using OneHotEncoding

Created new features:

tenure_group: binned tenure values

contract_type: derived from contract plan
```
categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService',
                    'MultipleLines', 'InternetService', 'OnlineSecurity',
                    'OnlineBackup', 'DeviceProtection', 'TechSupport',
                    'StreamingTV', 'StreamingMovies', 'Contract',
                    'PaperlessBilling', 'PaymentMethod', 'contract_type', 'tenure_group']

df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

Saved feature columns:

import joblib
joblib.dump(df_encoded.columns.tolist(), 'model/columns.pkl')
```
Screenshot
![Snap_7](https://i.postimg.cc/nhGWy5d1/Correlation-Matrix.png)

![Snap_8](https://i.postimg.cc/TPPtZP5R/Feature-Engineering.png)

![Snap_9](https://i.postimg.cc/PqcQ9Qk4/Feature-and-Churn-Risk.png)

💡 3. Model Building

Split data using train_test_split

![Snap_10](https://i.postimg.cc/3xfX0FWT/Evaluation.png)

Used RandomForestClassifier and XGBClassifier

![Snap_11](https://i.postimg.cc/1zgpGVNN/Rf-Confusion-Matrix.png)

Combined both in a VotingClassifier ensemble

![Snap_12](https://i.postimg.cc/k5kWfMxY/Evaluation-for-hybrid-model.png)


🚀 4. Streamlit App

Built a frontend app to:

Input limited user fields (tenure, contract, payment method)

Return churn risk + probability

cd app
streamlit run app.py

predictor.py:
```
def predict_churn(user_input_df):
    df_encoded = pd.get_dummies(user_input_df)
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)
    prob = model.predict_proba(df_encoded)[:, 1][0]
    return int(prob >= 0.55), prob
```

![Snap_13](https://i.postimg.cc/h4wRsHwz/Stream-lit-app.png)
![Snap_14](https://i.postimg.cc/mZcgTNW9/App-output.png)

📊 6. Power BI Dashboard

Used predicted churn probability + actual data to build:

Churn Funnel: Tracks conversion to churn

Matrix: Contract x Tenure x Payment

Slicers: Gender, Internet Type, Region

Gauge: Churn % vs Safe Users

Insights Table: Segment-wise average churn risk

Screenshot:


![Snap_15](https://i.postimg.cc/GtM2gzW3/Pwer-Bi-Dashboard.png)
