import streamlit as st
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from utils import load_data

df = load_data()

st.title("📈 Advanced Analytics")

features = [
    "danceability",
    "energy",
    "valence",
    "tempo",
    "acousticness"
]

data = df[features].dropna()

kmeans = KMeans(
    n_clusters=5,
    random_state=42
)

clusters = kmeans.fit_predict(data)

pca = PCA(n_components=2)

reduced = pca.fit_transform(data)

plot_df = data.copy()

plot_df["x"] = reduced[:, 0]
plot_df["y"] = reduced[:, 1]
plot_df["cluster"] = clusters

fig = px.scatter(
    plot_df,
    x="x",
    y="y",
    color="cluster",
    title="Song Clusters"
)

st.plotly_chart(fig, use_container_width=True)
