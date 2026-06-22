# 📊 Invoice Intelligence System

An end-to-end Machine Learning application designed to automate vendor invoice analysis by predicting freight costs and identifying potentially risky invoices requiring manual review.

Built using **Python, Scikit-Learn, SQLite, and Streamlit**, this project demonstrates a production-style ML workflow including data preprocessing, model training, evaluation, inference, and deployment through an interactive web application.

---

## 🚀 Features

### 🚚 Freight Cost Prediction

Predict expected freight charges for vendor invoices using historical procurement and logistics data.

### ⚠️ Invoice Risk Detection

Identify invoices that may require manual review by analyzing discrepancies between invoice information and purchase records.

### 📈 Interactive Dashboard

Built with Streamlit for real-time predictions and user-friendly interaction.

### 🤖 Machine Learning Pipeline

Includes:

* Data extraction from SQLite database
* Feature engineering
* Data preprocessing and scaling
* Model training and evaluation
* Model persistence using Joblib
* Real-time inference

---

## 🏗️ Project Architecture

```text
Vendor Invoice Data
        │
        ▼
 Data Preprocessing
        │
        ▼
 Feature Engineering
        │
        ▼
 Machine Learning Models
        │
 ┌──────┴──────┐
 ▼             ▼

Freight      Invoice
Prediction   Flagging
```

---

## 📂 Project Structure

```text
Invoice Intelligence Project
│
├── data/
│   └── inventory.db
│
├── Freight Prediction Cost/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   └── models/
│
├── Invoice Flagging/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   └── models/
│
├── Inference/
│   ├── Predict_freight.py
│   └── Predict_invoice.py
│
├── models/
│   ├── predict_freight_model1.pkl
│   ├── predict_flag_invoice1.pkl
│   └── scaler1.pkl
│
├── pages/
│   ├── freight_prediction.py
│   └── invoice_flagging.py
│
└── app.py
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* SQLite
* Joblib
* Streamlit

---

## 📊 Machine Learning Models

### Freight Cost Prediction

* Model: Random Forest Regressor
* Objective: Estimate freight cost from invoice attributes

### Invoice Risk Detection

* Model: Random Forest Classifier
* Objective: Classify invoices as:

  * Low Risk
  * High Risk

---

## 📈 Model Performance

### Invoice Risk Detection

| Metric    | Score                   |
| --------- | ----------------------- |
| Accuracy  | ~88%                    |
| Precision | High                    |
| Recall    | ~96% for risky invoices |
| F1 Score  | Strong performance      |

The model successfully identifies the vast majority of risky invoices while maintaining strong overall accuracy.

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/invoice-intelligence-system.git

cd invoice-intelligence-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser and provide access to:

* Freight Cost Prediction
* Invoice Risk Detection

---

## 🎯 Business Impact

This project demonstrates how machine learning can assist procurement and finance teams by:

* Automating invoice review processes
* Detecting potentially anomalous invoices
* Reducing manual effort
* Improving operational efficiency
* Supporting data-driven procurement decisions

---

