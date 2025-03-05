import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
from surprise import Reader, Dataset, SVD

# Load Data
def load_data():
    place_df = pd.read_csv("eco_place.csv")
    ratings_df = pd.read_csv("eco_rating.csv")
    merged_df = place_df.merge(ratings_df, on="place_id")
    return merged_df

# Train Model
def train_model(df):
    kolomnya = df[['user_id', 'place_name', 'rating']]
    data = Dataset.load_from_df(kolomnya, Reader())
    trainset = data.build_full_trainset()
    model = SVD()
    model.fit(trainset)
    return model, kolomnya

# Predict Recommendations
def get_recommendations(user_id, model, kolomnya):
    semuawisata = kolomnya.place_name.unique()
    terrating = kolomnya[kolomnya.user_id == user_id].place_name
    belumrating = [wisata for wisata in semuawisata if wisata not in terrating]
    skor = [(wisata, model.predict(user_id, wisata).est) for wisata in belumrating]
    skor_urut = sorted(skor, key=lambda x: x[1], reverse=True)
    return skor_urut[:3]

# Streamlit UI
st.title("🌿 EcoTourism Recommendation System")

st.write("Upload the eco_place.csv and eco_rating.csv files to proceed.")

place_file = st.file_uploader("Upload eco_place.csv", type=["csv"])
rating_file = st.file_uploader("Upload eco_rating.csv", type=["csv"])

if place_file and rating_file:
    place_df = pd.read_csv(place_file)
    ratings_df = pd.read_csv(rating_file)
    df = place_df.merge(ratings_df, on="place_id")
    st.write("### Dataset Preview")
    st.dataframe(df.head())
    
    st.write("### Training Model...")
    model, kolomnya = train_model(df)
    st.success("Model training complete!")
    
    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    
    if st.button("Get Recommendations"):
        recommendations = get_recommendations(user_id, model, kolomnya)
        st.write("### Top 3 Recommended EcoTourism Places")
        for wisata, nilai in recommendations:
            st.write(f"- {wisata} (Predicted Rating: {nilai:.2f})")