import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Tracks", len(df))

with col2:
    st.metric("Genres", df["track_genre"].nunique())

with col3:
    st.metric("Artists", df["artists"].nunique())

with col4:
    st.metric(
        "Avg Popularity",
        round(df["popularity"].mean(), 2)
    )

st.divider()

genre_count = (
    df["track_genre"]
    .value_counts()
    .head(15)
)

fig = px.bar(
    genre_count,
    title="Top Genres"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.histogram(
    df,
    x="popularity",
    nbins=30,
    title="Popularity Distribution"
)

st.plotly_chart(fig2, use_container_width=True)
