
# 🏏 IPL Winning Team Predictor using Machine Learning

This project was completed as part of my **AI/ML Internship** at **InternPe**. The task involved building and deploying a machine learning model that predicts the **winning team** in an IPL match based on real-time match statistics like score, overs, wickets, and more.

---

## 📌 Task Objective

Develop and deploy a **classification/regression-based machine learning model** to predict the outcome of an IPL match using historical ball-by-ball data. The final solution is deployed as an interactive **Streamlit web application**.

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas  
- NumPy  
- scikit-learn  
  - Random Forest Regressor (for score prediction)  
  - Train-Test Split, Evaluation Metrics  
- Matplotlib / Seaborn (for EDA)  
- Jupyter Notebook  
- Pickle & JSON (for model & feature saving)

---

## 📁 Project Structure

```

ipl-winning-predictor/
│
├── IPL\_WinningPrediction.ipynb       # Jupyter Notebook for model training
├── ipl\_colab.xlsx                    # Raw IPL dataset
├── ipl\_score\_predictor.pkl           # Trained ML model
├── model\_features.json               # Feature columns used in training
├── app.py                            # Streamlit app for prediction
├── README.md                         # Project documentation

```

---

## 🏏 Dataset Description

The dataset contains ball-by-ball details of IPL matches from 2008 onwards. Extracted and cleaned to create useful features for modeling.

Key Features Used:

- `runs`, `wickets`, `overs`  
- `runs_last_5`, `wickets_last_5`  
- `batting_team`, `bowling_team` (one-hot encoded)  
- `year`, `month`, `day`  

---

## 🔄 ML Workflow

1. **Data Cleaning** – Filter consistent teams and match dates  
2. **Feature Engineering** – Extract innings-level statistics  
3. **Encoding** – One-hot encode categorical features  
4. **Model Training** – Trained a `RandomForestRegressor` to predict total score  
5. **Model Saving** – Saved using `pickle` and `json`  
6. **Web Deployment** – Streamlit app for real-time prediction

---

## 🖥️ Web App Features

- Select **Batting Team** and **Bowling Team**  
- Enter **Runs, Wickets, Overs**, and **Last 5 Overs Stats**  
- Choose **Match Date**  
- Get:
  - 🎯 Predicted Final Score  
  - 🏆 Likely Winning Team  
- Clean and modern UI built using Streamlit

---

## 📷 Screenshot

![App Screenshot](IPLWinningPredictor.png) <!-- Add your screenshot filename here -->

---

## 🔧 Future Scope

- Train a classifier model for **win probability** (instead of score)
- Add second innings logic for deeper match analysis  
- Enhance visualizations (run rate graph, win % chart)  
- Deploy online (Streamlit Cloud, Hugging Face Spaces)

---

## 🎓 Internship & Task Details

- **Internship Track**: Artificial Intelligence & Machine Learning  
- **Internship Provider**: InternPe  
- **Task Name**: Task 03 – IPL Winning Team Predictor  
- **Environment**: Jupyter Notebook + Streamlit App (Local)

---

## 📬 Contact

**Difina George**  
📧 difina.georgecs@gmail.com  
📍 Kerala, India


