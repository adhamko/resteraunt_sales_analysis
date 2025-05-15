# resteraunt_sales_analysis
# 🍽️ Restaurant Orders EDA & Visualization App

This project includes a **Streamlit web application** and a **Jupyter notebook** that help analyze and visualize restaurant order data. It’s designed to support exploratory data analysis (EDA), find insights, and create useful charts directly from your CSV files.

---

## 📁 Project Structure

.
├── order_app.py # Streamlit app for CSV upload, EDA, and visualizations
├── orders_menu.ipynb # Jupyter notebook for step-by-step EDA on restaurant data
├── requirements.txt # Required Python packages
├── sample_data/ # Optional folder for example CSVs
└── README.md # Project documentation

## 📊 1. Streamlit App — `order_app.py`

This interactive app lets users upload any `.csv` file and performs automatic EDA and plotting.

### 🔧 Features:

- Upload any CSV file
- Preview first few rows
- Check dataset shape and column types
- Generate summary statistics
- Detect and display missing values
- Show a correlation heatmap (numerical columns)
- Interactive chart options:
  - Scatter plot
  - Line chart
  - Bar chart
  - Histogram
  - Box plot

### ▶️ Run the App

```bash
streamlit run order_app.py

2. Jupyter Notebook — orders_menu.ipynb
This notebook contains a detailed EDA on restaurant order and menu datasets. It includes:

Reading and inspecting CSV files

Merging datasets

Handling null values

Visualizing order trends

Analyzing top-selling items, popular categories, etc.

Insights and recommendations
 Use Cases
Restaurant sales and inventory analysis

Quick data profiling for any dataset

Dashboard creation for non-programmers

Educational purposes for learning EDA
