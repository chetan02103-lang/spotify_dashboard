import streamlit as st
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

from utils import load_data

df = load_data()

st.title("🤖 Song Recommendations")

features = [
    "danceability",
    "energy",
    "valence",
    "tempo",
    "acousticness"
]

sample = df.dropna(subset=features)

scaler = StandardScaler()

X = scaler.fit_transform(sample[features])

similarity = cosine_similarity(X)

song = st.selectbox(
    "Select Song",
    sample["track_name"].unique()
)

if st.button("Recommend"):

    idx = sample[
        sample["track_name"] == song
    ].index[0]

    scores = list(
        enumerate(similarity[idx])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )[1:11]

    recommendations = [
        sample.iloc[i[0]]["track_name"]
        for i in scores
    ]

    st.write(recommendations)
