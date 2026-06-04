import pandas as pd
import streamlit as st

DATA_PATH = "data/spotify-tracks-dataset.csv"

@st.cache_data
def load_data():
    """
    Load and preprocess Spotify dataset.
    """

    df = pd.read_csv(DATA_PATH)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna(subset=["track_name", "artists"])

    return df


def get_audio_features():
    return [
        "danceability",
        "energy",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo"
    ]


def get_top_artists(df, n=20):
    return (
        df.groupby("artists")["popularity"]
        .mean()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


def get_top_genres(df, n=15):
    return (
        df["track_genre"]
        .value_counts()
        .head(n)
        .reset_index()
    )
