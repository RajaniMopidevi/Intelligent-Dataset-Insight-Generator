import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="Intelligent Dataset Insight Generator",
    layout="wide"
)

st.title("Intelligent Dataset Insight Generator")
st.write("Upload a CSV file to begin analysis.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

   
    # Dataset Preview
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

  
    # Column Data Types
   
    st.subheader("Column Data Types")

    dtypes_df = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.values
    }).reset_index(drop=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.dataframe(dtypes_df, use_container_width=True)

 
    # Missing Value Analysis
   
    st.subheader("Missing Value Analysis")

    missing_values = df.isnull().sum()
    missing_percentage = ((missing_values / len(df)) * 100).round(2)

    missing_df = pd.DataFrame({
        "Column Name": df.columns,
        "Missing Values": missing_values.values,
        "Percentage (%)": missing_percentage.values
    }).reset_index(drop=True)

    missing_df = missing_df[missing_df["Missing Values"] > 0]

    col1, col2 = st.columns([3, 2])
    with col1:
        if missing_df.empty:
            st.success("No missing values detected.")
        else:
            st.dataframe(
                missing_df.sort_values(by="Percentage (%)", ascending=False),
                use_container_width=True
            )
  
    # Statistical Summary

    st.subheader("Statistical Summary")

    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    # Numerical Summary 
    if len(numerical_cols) > 0:
        st.markdown("### Numerical Columns Summary")

        numerical_summary = df[numerical_cols].describe().T
        numerical_summary["skewness"] = df[numerical_cols].skew()

        col1, col2 = st.columns([3, 2])
        with col1:
            st.dataframe(numerical_summary.round(2), use_container_width=True)

    # Categorical Summary
    if len(categorical_cols) > 0:
        st.markdown("### Categorical Columns Summary")

        categorical_summary = pd.DataFrame({
            "Unique Values": df[categorical_cols].nunique(),
            "Most Frequent": df[categorical_cols].mode().iloc[0],
            "Missing Values": df[categorical_cols].isnull().sum()
        })

        col1, col2 = st.columns([3, 2])
        with col1:
            st.dataframe(categorical_summary, use_container_width=True)        

  
 
    # Correlation Analysis

    st.subheader("Correlation Heatmap")

    # Select numerical columns
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

    # Remove obvious ID columns
    numerical_cols = [col for col in numerical_cols if "id" not in col.lower()]

    if len(numerical_cols) > 1:
        import matplotlib.pyplot as plt
        import seaborn as sns

        corr_matrix = df[numerical_cols].corr()

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            linewidths=0.5,
            ax=ax
        )

        col1, col2 = st.columns([3, 2])
        with col1:
            st.pyplot(fig)
    else:
        st.info("Not enough numerical columns for correlation analysis.")        
        
    # Outlier Detection (IQR Method)

    st.subheader("Outlier Detection (IQR Method)")

    if len(numerical_cols) > 0:

        outlier_data = []

        # Remove ID-like columns for outlier detection
        clean_numerical_cols = [
            col for col in numerical_cols
            if "id" not in col.lower() and "unnamed" not in col.lower()
        ]

        for col in clean_numerical_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

            outlier_data.append({
                "Column Name": col,
                "Outlier Count": len(outliers)
            })

        outlier_df = pd.DataFrame(outlier_data)

        col1, col2 = st.columns([3, 2])

        with col1:
            st.dataframe(outlier_df, use_container_width=True)

    else:
        st.info("No numerical columns available for outlier detection.")

    # AI Insight Generator
    st.divider()
    st.subheader("AI-Generated Insights")

    if st.button("Generate AI Insights"):

        # Prepare structured dataset summary
        dataset_summary = f"""
        Rows: {df.shape[0]}
        Columns: {df.shape[1]}
        Numerical Columns: {len(numerical_cols)}
        Categorical Columns: {len(categorical_cols)}
        Columns with Missing Values: {len(missing_df)}
        Columns with Outliers: {(outlier_df['Outlier Count'] > 0).sum()}
        """

        prompt = f"""
            You are a senior Data Analyst.

            Based strictly on the dataset summary below, generate analytical insights.

            Dataset Summary:
            {dataset_summary}

            Provide:

            1. Key data-driven business insights
            2. Data quality issues detected
            3. Specific preprocessing recommendations
            4. Modeling readiness assessment

            Keep the tone analytical and concise.
            Do not include greetings or conversational language.
            """

        with st.spinner("Generating AI insights... Please wait"):

            try:
                response = requests.post(
                    "http://localhost:11434/api/chat",
                    json={
                        "model": "phi",
                        "messages": [
                            {"role": "user", "content": prompt}
                        ],
                        "stream": False
                    },
                    timeout=120
                )

                result = response.json()
                ai_output = result["message"]["content"]

                st.markdown(ai_output)

            except Exception as e:
                st.error(f"Error: {e}")