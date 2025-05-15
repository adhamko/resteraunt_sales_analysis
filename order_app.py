import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="EDA & Visualization App", layout="wide")

st.title("📊 Data Upload, EDA, and Visualization App")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.write(df.head())

    # Basic Info
    st.subheader("Dataset Information")
    st.write(f"Shape of the dataset: {df.shape}")
    st.write("Column Names and Types:")
    st.write(df.dtypes)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    if not numeric_df.empty:
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Visualization
    st.subheader("Create Visualizations")

    chart_type = st.selectbox("Choose a Chart Type", ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot"])

    columns = df.columns.tolist()
    x_col = st.selectbox("X-axis", columns)
    y_col = st.selectbox("Y-axis", columns, index=1 if len(columns) > 1 else 0)

    if chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_col, y=y_col, title="Scatter Plot")
    elif chart_type == "Line Chart":
        fig = px.line(df, x=x_col, y=y_col, title="Line Chart")
    elif chart_type == "Bar Chart":
        fig = px.bar(df, x=x_col, y=y_col, title="Bar Chart")
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_col, title="Histogram")
    elif chart_type == "Box Plot":
        fig = px.box(df, x=x_col, y=y_col, title="Box Plot")

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Please upload a CSV file to get started.")
