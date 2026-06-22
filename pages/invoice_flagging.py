import streamlit as st
from Inference.Predict_invoice import predict_invoice_flag

st.set_page_config(
    page_title="Invoice Flagging",
    page_icon="⚠",
    layout="wide"
)

st.title("⚠ Invoice Risk Detection")

c1,c2 = st.columns(2)

with c1:

    invoice_quantity = st.number_input(
        "Invoice Quantity",
        min_value=0
    )

    invoice_dollars = st.number_input(
        "Invoice Dollars",
        min_value=0.0
    )

    freight = st.number_input(
        "Freight",
        min_value=0.0
    )

with c2:

    total_item_quantity = st.number_input(
        "Total Item Quantity",
        min_value=0
    )

    total_item_dollars = st.number_input(
        "Total Item Dollars",
        min_value=0.0
    )

if st.button(
    "Analyze Invoice",
    use_container_width=True
):

    data = {
        "invoice_quantity":[invoice_quantity],
        "invoice_dollars":[invoice_dollars],
        "Freight":[freight],
        "total_item_quantity":[total_item_quantity],
        "total_item_dollars":[total_item_dollars]
    }

    result = predict_invoice_flag(data)

    pred = result[
        "Predicted_Flag"
    ].iloc[0]

    if pred == 1:

        st.error("""
        🚨 HIGH RISK

        Invoice should be reviewed manually.
        """)

    else:

        st.success("""
        ✅ LOW RISK

        Invoice can proceed normally.
        """)

if st.button("⬅ Back to Dashboard"):
    st.switch_page("app.py")