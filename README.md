## Intelligent Dataset Insight Generator  

An AI-powered data analysis dashboard built using **Streamlit** and **Pandas**. The application allows users to upload any CSV dataset and automatically perform exploratory data analysis (EDA), detect data quality issues, visualize correlations, and generate AI-driven analytical insights.  

This project was built to strengthen hands-on skills in data profiling, statistical analysis, visualization, and integrating local LLMs into real-world data applications.

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
- Column data type identification  
- Missing value analysis with percentage calculation  
- Numerical statistical summary with skewness  
- Categorical summary (unique values, most frequent value)  
- Correlation heatmap visualization using Seaborn  
- Outlier detection using the IQR method  
- AI-generated:
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

### Project Structure

Intelligent-Dataset-Insight-Generator/
│

├── app.py                  

├── requirements.txt        

├── assets/                 

│   ├── 01_dashboard_overview.png

│   ├── 02_column_data_types.png

│   ├── 03_missing_value_analysis.png

│   ├── 04_numerical_columns_summary.png

│   ├── 05_categorical_columns_summary.png

│   ├── 06_correlation_heatmap.png

│   ├── 07_outlier_detection_iqr.png

│   └── 08_ai_generated_insights.png

└── README.md               

### Future Improvements

- Export complete EDA report as PDF
- Add automated preprocessing pipeline
- Enable cleaned dataset download
- Add feature importance suggestions
- Deploy using Streamlit Cloud or Docker
- Add authentication for multi-user access
