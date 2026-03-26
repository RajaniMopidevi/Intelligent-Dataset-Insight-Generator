## Intelligent Dataset Insight Generator  

An AI-powered data analysis application built using **Streamlit** and **Pandas** that automates exploratory data analysis (EDA) and generates meaningful insights from structured datasets.

The application allows users to upload CSV datasets and instantly perform data profiling, detect data quality issues, visualize relationships, and generate **AI-driven insights using a local LLM**.

This project focuses on reducing manual effort in data exploration by transforming raw datasets into structured, interpretable insights for faster and more efficient decision-making.

---

## Demo  

### Dashboard Overview  
![Dashboard Overview](assets/01_dashboard_overview.png)

### Column Data Types  
![Column Data Types](assets/02_column_data_types.png)

### Missing Value Analysis  
![Missing Value Analysis](assets/03_missing_value_analysis.png)

### Numerical Columns Summary  
![Numerical Columns Summary](assets/04_numerical_columns_summary.png)

### Categorical Columns Summary  
![Categorical Columns Summary](assets/05_categorical_columns_summary.png)

### Correlation Heatmap  
![Correlation Heatmap](assets/06_correlation_heatmap.png)

### Outlier Detection (IQR Method)  
![Outlier Detection (IQR Method)](assets/07_outlier_detection_iqr.png)

### AI-Generated Insights  
![AI-Generated Insights](assets/08_ai_generated_insights.png)

---

## Features  

- Upload any CSV dataset for automated analysis  
- Automatic dataset preview (top records)  
- Column data type detection 
- Missing value analysis with percentage insights 
- Numerical statistics (mean, median, skewness)
- Categorical summary (unique values,frequency distribution)  
- Correlation heatmap visualization 
- Outlier detection using the IQR method  
- AI-powered insights using a local LLM:
  - Business insights  
  - Data quality issues  
  - Preprocessing recommendations  
  - Modeling readiness assessment  

---

## Tech Stack  

- Python  
- Streamlit  
- Pandas  
- Matplotlib  
- Seaborn  
- Requests  
- Local LLM (Ollama - phi model)  

---

## How to Run Locally  

1. Clone the repository:
```bash
git clone https://github.com/RajaniMopidevi/Intelligent-Dataset-Insight-Generator.git
```
2. Navigate to the project folder:
```bash
cd Intelligent-Dataset-Insight-Generator
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Ensure Ollama is running locally:
```bash
ollama run phi
```
5. Run the Streamlit app:
```bash
streamlit run app.py
```
or 
```bash
python -m streamlit run app.py
```

---

### Project Structure

app.py        → Main application (UI + EDA logic)
assets/       → Screenshots for README demo
requirements.txt → Project dependencies
README.md     → Project documentation  

---

### Future Improvements

- Export full EDA report as PDF
- Add automated preprocessing pipeline
- Enable cleaned dataset download
- Introduce feature importance suggestions
- Deploy using Streamlit Cloud or Docker
- Add authentication for multi-user access
