import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Setup
st.set_page_config(page_title="Trader Behavior Dashboard", layout="wide")
st.title("Trader Behavior vs Market Sentiment")

# Load Data
final_df = pd.read_csv("Datasets/Visualisations/final_features_data.csv")
cluster_df = pd.read_csv("Datasets/Visualisations/clustered_data.csv")


# Sidebar Filters
st.sidebar.header("Filters")
sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    final_df['classification'].unique()
)

cluster = st.sidebar.selectbox(
    "Select Cluster",
    sorted(cluster_df['cluster'].unique())
)

# Tabs
tab1, tab2 = st.tabs(["Sentiment Analysis", "Clustering Analysis"])

# TAB 1 : Sentiment
with tab1:
    st.subheader("Performance by Sentiment")

    filtered_sentiment = final_df[
        final_df['classification'] == sentiment
    ]

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        sns.histplot(filtered_sentiment['daily_pnl'], kde=True, ax=ax1)
        ax1.set_title("PnL Distribution")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        sns.histplot(filtered_sentiment['risk_score'], kde=True, ax=ax2)
        ax2.set_title("Risk Score Distribution")
        st.pyplot(fig2)

    st.subheader("Summary Stats")
    st.write(filtered_sentiment.describe())

# TAB 2: Clustering
with tab2:
    st.subheader("Cluster-Based Analysis")

    filtered_cluster = cluster_df[
        cluster_df['cluster'] == cluster
    ]

    col3, col4 = st.columns(2)

    with col3:
        fig3, ax3 = plt.subplots()
        sns.histplot(filtered_cluster['daily_pnl'], kde=True, ax=ax3)
        ax3.set_title("PnL Distribution (Cluster)")
        st.pyplot(fig3)

    with col4:
        fig4, ax4 = plt.subplots()
        sns.histplot(filtered_cluster['risk_score'], kde=True, ax=ax4)
        ax4.set_title("Risk Score Distribution (Cluster)")
        st.pyplot(fig4)

    st.subheader("Cluster Summary")
    st.write(filtered_cluster.describe())