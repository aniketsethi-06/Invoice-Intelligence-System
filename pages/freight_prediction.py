# pages/1_Freight_Prediction.py

import streamlit as st
from Inference.Predict_freight import predict_freight_cost

st.set_page_config(
    page_title="Freight Prediction",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Freight Cost Prediction")

st.write(
    "Estimate freight charges using the trained ML model."
)

amount = st.number_input(
    "Invoice Amount ($)",
    min_value=0.0
)

if st.button(
    "Predict Freight Cost",
    use_container_width=True
):

    data = {
        "Dollars":[amount]
    }

    result = predict_freight_cost(data)

    prediction = result[
        "Predicted_Freight"
    ].iloc[0]

    st.success(
        f"Predicted Freight Cost: ${prediction:,.2f}"
    )

if st.button("⬅ Back to Dashboard"):
    st.switch_page("app.py")
