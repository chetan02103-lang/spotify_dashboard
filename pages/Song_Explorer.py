import streamlit as st
from utils import load_data

df = load_data()

st.title("🔍 Song Explorer")

genre = st.selectbox(
    "Genre",
    sorted(df["track_genre"].unique())
)

popularity = st.slider(
    "Minimum Popularity",
    0,
    100,
    50
)

filtered = df[
    (df["track_genre"] == genre)
    &
    (df["popularity"] >= popularity)
]

st.dataframe(filtered)

csv = filtered.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "songs.csv"
)
