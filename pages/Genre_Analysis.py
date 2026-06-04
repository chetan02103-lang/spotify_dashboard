import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("🎼 Genre Analysis")

genre = st.selectbox(
    "Select Genre",
    sorted(df["track_genre"].unique())
)

filtered = df[df["track_genre"] == genre]

st.write(filtered.head())

audio_cols = [
    "danceability",
    "energy",
    "valence",
    "acousticness",
    "instrumentalness"
]

avg = filtered[audio_cols].mean()

fig = px.bar(
    x=avg.index,
    y=avg.values,
    title=f"{genre} Audio Profile"
)

st.plotly_chart(fig, use_container_width=True)
