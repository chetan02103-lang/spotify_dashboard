import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("🎧 Audio Features")

features = [
    "danceability",
    "energy",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence"
]

feature = st.selectbox(
    "Select Feature",
    features
)

fig = px.histogram(
    df,
    x=feature,
    title=f"{feature} Distribution"
)

st.plotly_chart(fig, use_container_width=True)

corr = df[features].corr()

fig2 = px.imshow(
    corr,
    text_auto=True,
    title="Feature Correlation"
)

st.plotly_chart(fig2, use_container_width=True)
