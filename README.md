# Student Score Prediction

A machine learning project that predicts student exam scores based on study hours using Linear and Polynomial Regression.

## Project Overview

This project analyzes student performance data and builds a prediction model to estimate exam scores based on study time. It includes:

- **Data Analysis**: Exploratory data analysis on student performance factors
- **Machine Learning Models**: Linear Regression and Polynomial Regression
- **Web Application**: Interactive Streamlit dashboard for predictions

## Tech Stack

- **Python**
- **Jupyter Notebook**
- **Streamlit** - Web app framework
- **Scikit-learn** - Machine learning
- **Pandas** - Data manipulation
- **Matplotlib** - Data visualization

## Project Structure

| File | Description |
|------|-------------|
| `Student_Score_Prediction.ipynb` | Jupyter notebook with data analysis and model training |
| `app.py` | Streamlit web application for predictions |
| `student_prediction_model.pkl` | Pre-trained prediction model |
| `README.md` | Project documentation |

## Getting Started

### Prerequisites

- Python 3.7+
- Required packages:
  ```bash
  pip install streamlit scikit-learn pandas matplotlib numpy joblib
  ```

### Running the Web App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

### Running the Notebook

Open `Student_Score_Prediction.ipynb` in Jupyter Lab or Google Colab to:
- Load and explore the dataset
- Train and evaluate models
- View visualizations

## Features

- **Interactive Slider**: Adjust study time (0-20 hours/week)
- **Real-time Predictions**: Get instant score predictions
- **Visualization**: See how study time affects predicted scores
- **Model Comparison**: Compare Linear vs Polynomial Regression performance

## Dataset

The project uses `StudentPerformanceFactors.csv` containing:
- Hours Studied
- Exam Score
- Other performance-related factors

## Model Details

- **Algorithm**: Linear Regression / Polynomial Regression (degree=2)
- **Input**: Study time (hours/week)
- **Output**: Predicted exam score
- **Evaluation Metrics**: R² Score, Mean Squared Error

## Usage Tips

1. Use the slider to adjust study hours
2. Click "Predict" to see the estimated exam score
3. View the chart to understand how different study hours impact scores


## License

This project is for educational purposes.

