import streamlit as st
from PIL import Image

# ---- Header Section ----
st.title("🏡 Real Estate AI Platform")
st.subheader("Smarter Decisions • Accurate Predictions • Personalized Recommendations")

st.markdown("""
Welcome to **Real Estate AI**, an intelligent platform designed to empower **homebuyers, investors, and real estate professionals**.  
Our solution combines **data-driven analytics, price prediction models, and personalized recommendations** to make property decisions **smarter, faster, and more reliable**.
""")

# ---- Hero Image ----
# hero_img = Image.open("Real_estate_app\images\Screenshot 2025-09-15 183046.png")  # Replace with your own image path
# st.image(hero_img, use_container_width=True)

st.markdown("---")

# ---- Key Features Section ----
st.header("✨ What We Offer")

col1, col2, col3 = st.columns(3)

with col1:
    # st.image("Real_estate_app\images\Screenshot 2025-09-15 183220.png", use_container_width=True)  # Replace with your image
    st.subheader("📊 Real Estate Analytics")
    st.write("""
    - Explore property trends across **129+ sectors**  
    - Interactive maps with **price per sq.ft. heatmaps**  
    - Insights on **BHK distribution, built-up areas, house vs flat trends**  
    """)

with col2:
    # st.image("images/price_prediction.jpg", use_container_width=True)  # Replace with your image
    st.subheader("💰 Price Prediction")
    st.write("""
    - AI-driven models trained on **thousands of property listings**  
    - Predict **fair property prices** with high accuracy (R² ≈ 0.89)  
    - Factors include **location, size, amenities, and more**  
    """)

with col3:
    # st.image("images/recommendation.jpg", use_container_width=True)  # Replace with your image
    st.subheader("🤝 Smart Recommendations")
    st.write("""
    - Personalized property suggestions using **AI similarity search**  
    - Matches based on **features, location advantages, and amenities**  
    - Helps buyers & investors find the **best-fit property**  
    """)

st.markdown("---")

# ---- Why Choose Us Section ----
st.header("🚀 Why Choose Our Platform?")
st.markdown("""
- ✅ **Accurate** – Advanced ML models like Random Forest & XGBoost ensure reliability  
- ✅ **User-Friendly** – Simple, intuitive, and interactive visualizations  
- ✅ **Personalized** – Tailored recommendations for every buyer  
- ✅ **Comprehensive** – From analytics to prediction to recommendations, all in one place  
""")

# ---- Call to Action ----
st.markdown("---")
st.subheader("Ready to explore smarter property insights?")
st.success("🔎 Use the sidebar to start exploring Analytics, Price Prediction, or Recommendations!")
