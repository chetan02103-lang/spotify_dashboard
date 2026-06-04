import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("🎤 Artist Analytics")

top_artists = (
    df.groupby("artists")
    ["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(20)
)

fig = px.bar(
    top_artists,
    title="Top Artists by Popularity"
)

st.plotly_chart(fig, use_container_width=True)
