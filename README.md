# 🏏 IPL First Innings Score Predictor using Machine Learning

This project was completed as part of my **AI/ML Internship** at **InternPe**. The task involved building and deploying a machine learning model that predicts the **final score** in the **first innings** of an IPL match using real-time match inputs like runs, overs, wickets, and recent performance.

---

## 📌 Task Objective

Develop and deploy a **regression-based ML model** to forecast the total score in the **first innings** of an IPL match. The final solution includes a **Streamlit-powered web application** that accepts real-time match inputs and returns a live score prediction.

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas  
- NumPy  
- scikit-learn  
  - Random Forest Regressor  
  - Train-Test Split  
  - Evaluation Metrics  
- Jupyter Notebook  
- Pickle / JSON (for model saving)

---

## 📁 Project Structure
```
ipl-first-innings-predictor/
│
├── IPL_WinningPrediction.ipynb # Jupyter Notebook for model training
├── ipl_colab.xlsx # Raw IPL dataset
├── ipl_score_predictor.pkl # Trained ML model
├── model_features.json # Feature columns used in training
├── app.py # Streamlit web app for predictions
├── README.md # Project documentation

```
---

## 🏏 Dataset Description

The dataset includes ball-by-ball information for IPL matches between 2008–2023, processed into innings-level data.

Key features used for prediction:

- `runs`, `wickets`, `overs`  
- `runs_last_5`, `wickets_last_5`  
- `batting_team`, `bowling_team` (one-hot encoded)  
- `year`, `month`, `day`  

---

## 🔄 ML Workflow

1. Data cleaning and filtering consistent teams  
2. One-hot encoding of team names  
3. Feature selection based on match state  
4. Model training with `RandomForestRegressor`  
5. Model saving (`pickle`) and feature saving (`json`)  
6. Web interface using Streamlit for real-time prediction

---

## 🖥️ Web App Features

- Input real-time match stats: runs, overs, wickets, etc.  
- Select teams and match date  
- Predict the **final score for the first innings**  
- Displays likely winning team based on the predicted total  
- User-friendly UI with intuitive input widgets

---

## 📷 Screenshot

![App Screenshot](IPLFirstInningsPredictor.png) <!-- Add a screenshot if available -->

---

## 🔧 Future Scope

- Build separate predictor for second innings chase outcomes  
- Add run rate comparison visuals  
- Deploy online using Streamlit Cloud or Hugging Face  
- Enhance UI styling and animations

---

## 🎓 Internship & Task Details

- **Internship Track**: Artificial Intelligence & Machine Learning  
- **Internship Provider**: InternPe  
- **Task Name**: Task 03 – IPL First Innings Score Predictor  
- **Environment**: Jupyter Notebook + Streamlit App (Local)

---

## 📬 Contact

**Difina George**  
📧 difina.georgecs@gmail.com  
📍 Kerala, India
