# 🌿 EcoTourism Recommendation System

## 📌 Overview
This project builds a **recommendation system for ecotourism destinations** based on user ratings. The system utilizes **collaborative filtering with Singular Value Decomposition (SVD)** to predict user preferences and suggest top-rated ecotourism places.

## 🔧 Technologies Used
- **Python** (for data processing & modeling)
- **Pandas** (for data manipulation)
- **Matplotlib & Seaborn** (for visualization)
- **WordCloud** (for text analysis)
- **Surprise** (for recommendation system modeling)
- **Streamlit** (for web-based deployment)

## 📂 Dataset
This project requires two datasets:
1. **eco_place.csv** → Contains information about ecotourism places.
2. **eco_rating.csv** → Contains user ratings for different places.

## 🚀 How to Run
### 1️⃣ Install Dependencies
```bash
pip install streamlit pandas matplotlib seaborn wordcloud surprise
```
### 2️⃣ Run the Streamlit App
```bash
streamlit run nama_file.py
```
### 3️⃣ Upload Datasets
- Upload **eco_place.csv** and **eco_rating.csv** in the UI.

### 4️⃣ Get Recommendations
- Enter a **User ID** and click **Get Recommendations** to see the top 3 suggested ecotourism destinations.

## 🌐 Deployment with Streamlit
The system is deployed using **Streamlit**, allowing users to interactively explore recommended ecotourism destinations based on their ratings.

## 📊 Key Features
- **Collaborative Filtering Recommendation System** using **SVD**
- **User-Based Personalization** for eco-tourist recommendations
- **Interactive Visualization** of rating distributions

## 📝 Future Improvements
- Add content-based filtering to improve recommendations
- Implement a hybrid recommendation model
- Expand dataset with more user ratings and reviews

---
🔗 *Developed by Alvin Rahman Al Musyaffa*
