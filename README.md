# AI-Powered-Real-Estate-Intelligence-Platform-
> A complete end-to-end Data Science platform for real estate that provides **market analytics**, **price prediction**, and a **hybrid recommendation system** — deployed as an interactive app.  

---

## 🚀 Overview  
This project covers the **full data science lifecycle**:  
- **Data Engineering** – web scraping, cleaning, feature engineering, encoding  
- **Analytics Module** – dashboards for pricing trends, sector heatmaps, furnishing & BHK insights  
- **Price Prediction Module** – machine learning models for property price estimation  
- **Recommendation System Module** – hybrid recommender for personalized property suggestions  
- **Deployment** – interactive **Streamlit app** integrating all modules  

---

## 📂 Dataset  
- Source: 99acres property listings (scraped)  
- Size: ~3,500+ records (flats & houses across Gurgaon)  
- Features: property type, sector, price, price_per_sqft, bedrooms, bathrooms, area, furnishing, age, floor, luxury score, facilities, location advantages, etc.  
- Additional: lat-long mapping for 129+ Gurgaon sectors  

---

## 🛠️ Tech Stack  
- **Languages**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Category Encoders, Matplotlib, Seaborn, Plotly  
- **NLP & Similarity**: TF-IDF, Cosine Similarity  
- **Deployment**: Streamlit  
- **Visualization**: Plotly, WordCloud, Geospatial Maps  

---

## 📊 Modules  

### 1️⃣ Analytics Module  
Interactive dashboards providing **exploratory insights** into the real estate market:  
- **Price Trends**: sector-wise price per sqft, distribution plots, outlier detection  
- **Geospatial Maps**: Gurgaon sector heatmap (average price & built-up area)  
- **Room & Furnishing Insights**: pie charts & bar plots (1BHK–5BHK split, semi/fully furnished)  
- **Word Clouds**: most common facilities & location advantages  

---

### 2️⃣ Price Prediction Module  
Machine learning pipeline for accurate property valuation:  
- **Feature Engineering**:  
  - Price normalization (Lakhs → Crores), built-up area conversion  
  - Luxury score, furnishing clusters (via KMeans), floor category  
  - Sector mapping & categorical encoding (OneHot, Ordinal, Target Encoding)  
- **Model Selection & Benchmarking**:  
  - Models: Linear Regression, Ridge, Lasso, SVR, Decision Tree, Random Forest, Extra Trees, Gradient Boosting, AdaBoost, MLP, XGBoost  
  - Evaluation:  
    - Cross-validation R² (10-fold)  
    - Mean Absolute Error (MAE) on test set  
- **Best Model:** Random Forest → **R² = 0.88, MAE ≈ 0.53 Cr**  
- **Deployment**: Streamlit form for entering property details → outputs predicted price range  

---

### 3️⃣ Recommendation System Module  
A **hybrid content-based recommender** that suggests similar properties:  
- **Facilities Similarity** – TF-IDF + Cosine Similarity on facilities text  
- **Price & Area Similarity** – scaled numerical features (price, area, rooms)  
- **Location Advantage Similarity** – normalized distances to schools, metro, malls, hospitals  
- **Hybrid Approach** – weighted combination of all similarities  
- **Output** – Top 5 most similar properties with details (price, sector, furnishing, luxury score)  

---

## 📈 Results  
- **Prediction Accuracy**: Improved by **~18%** after feature engineering  
- **Best Model**: Random Forest (R² = 0.88, MAE ≈ 0.53 Cr)  
- **Analytics Impact**: Automated dashboards → **40% faster insights**  
- **Recommendation System**: Personalized top-5 similar property suggestions  

---
## 🔹 Screenshots 
<img width="1083" height="455" alt="image" src="https://github.com/user-attachments/assets/bcf6fda7-6f71-425e-add2-b9fe29b18c64" /> 
<img width="1002" height="561" alt="image" src="https://github.com/user-attachments/assets/76b8cba4-942d-4699-9e75-376e5541cd71" /> 
<img width="987" height="515" alt="image" src="https://github.com/user-attachments/assets/02a0bd2d-6e30-47fb-b957-e3b0d3cebdb3" /> 
<img width="1206" height="590" alt="image" src="https://github.com/user-attachments/assets/1b7a0520-3f20-4663-8486-2471692cdfde" /> 
<img width="968" height="770" alt="image" src="https://github.com/user-attachments/assets/d145ab96-44b3-4da5-a101-b73add555a39" /> 
<img width="1738" height="762" alt="image" src="https://github.com/user-attachments/assets/d61594db-9463-4025-bd02-fa36b5a8615f" />

## 🔹 Author
👤 Pranav Kapoor 







## 🗂️ Project Structure  
