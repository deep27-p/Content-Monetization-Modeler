import streamlit as st
import pandas as pd
import pickle

# ==============================
# 1. Page Config
# ==============================
st.set_page_config(
    page_title="LINEAR REGRESSION PREDICTION APP",
    page_icon="🌲",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f7f9fc;
        }
        .main {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .stButton>button {
            background-color: #2ecc71;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #27ae60;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# 2. Load Model
# ==============================
model = pickle.load(open("linear_regression_pipeline.pkl", "rb"))

# ==============================
# 3. Title
# ==============================
st.markdown("<h1>🌲 Linear regression Prediction App</h1>", unsafe_allow_html=True)
st.write("Fill in the details below and click **Predict** to see the output.")

# ==============================
# 4. Input Form
# ==============================
with st.form("prediction_form"):
    st.subheader("📌 Input Features")

    col1, col2 = st.columns(2)

    with col1:
        views = st.number_input("👁️ Views", value=0.0)
        likes = st.number_input("👍 Likes", value=0.0)
        comments = st.number_input("💬 Comments", value=0.0)
        watch_time = st.number_input("⏱️ Watch Time (minutes)", value=0.0)
    
    
    with col2:
        category = st.selectbox("📂 Category", ["Entertainment", "Education", "Technology", "Lifestyle"])
        device = st.selectbox("📱 Device", ["Mobile", "Desktop", "Tablet", "TV"])
        country = st.selectbox("🌍 Country", ["India", "USA", "UK", "Germany", "Canada"])
        engagement_rate = st.number_input("📊 Engagement Rate (%)", value=0.0)

    submitted = st.form_submit_button("🔮 Predict")

# Convert input into dataframe
input_data = pd.DataFrame({
    "views": [views],
    "likes": [likes],
    "comments": [comments],
    "watch_time_minutes": [watch_time],
    "category": [category],
    "device": [device],
    "country": [country],
    "engagement_rate": [engagement_rate]
})

# ==============================
# 5. Prediction
# ==============================
if submitted:
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Output: **{prediction[0]:.2f}**")