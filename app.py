import streamlit as st

st.set_page_config(
    page_title="Invoice Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#0B1120;
}

.hero{
    padding:40px;
    border-radius:20px;
    background:linear-gradient(
        135deg,
        #0F172A,
        #1E293B
    );
    border:1px solid #334155;
}

.metric-card{
    padding:25px;
    border-radius:15px;
    background:#111827;
    text-align:center;
}

.big-text{
    font-size:55px;
    font-weight:700;
}

.sub-text{
    font-size:20px;
    color:#94A3B8;
}

</style>
""", unsafe_allow_html=True)

# HERO SECTION

st.markdown("""
<div class="hero">

<div class="big-text">
📊 Invoice Intelligence System
</div>

<div class="sub-text">
AI-Powered Vendor Invoice Analytics Platform
</div>

<br>

Automate invoice review, detect risky transactions,
and forecast freight expenses using Machine Learning.

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# METRICS

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Models",
        "2"
    )

with c2:
    st.metric(
        "ML Algorithms",
        "Random Forest"
    )

with c3:
    st.metric(
        "Invoice Detection",
        "88%"
    )

with c4:
    st.metric(
        "Prediction Engine",
        "Live"
    )

st.divider()

st.subheader("Available Modules")

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    ### 🚚 Freight Cost Prediction

    Predict expected freight charges from
    vendor invoice amount using machine learning.

    #### Features

    - Freight forecasting
    - Cost optimization
    - Vendor benchmarking
    - Procurement planning
    """)

    if st.button(
        "Open Freight Prediction",
        use_container_width=True
    ):
        st.switch_page(
            "pages/Freight_Prediction.py"
        )

with col2:

    st.markdown("""
    ### ⚠ Invoice Risk Detection

    Automatically identify invoices
    requiring manual review.

    #### Features

    - Risk classification
    - Fraud detection
    - Cost anomaly detection
    - Approval prioritization
    """)

    if st.button(
        "Open Invoice Flagging",
        use_container_width=True
    ):
        st.switch_page(
            "pages/Invoice_Flagging.py"
        )
