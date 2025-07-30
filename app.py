import streamlit as st
import pandas as pd
import pickle
import json
from datetime import date

# Load model
with open('ipl_score_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

# Load feature columns
with open('model_features.json', 'r') as f:
    feature_columns = json.load(f)

# Team list (from training)
teams = [
    'Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]

# Title
st.title("🏏 IPL First Innings Score Predictor")

# --- Inputs ---
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", [team for team in teams if team != batting_team])

runs = st.number_input("Runs Scored", min_value=0)
wickets = st.number_input("Wickets Lost", min_value=0, max_value=10)
overs = st.number_input("Overs Completed", min_value=5.0, max_value=20.0, step=0.1)
runs_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0)
wickets_last_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, max_value=5)

match_date = st.date_input("Select Match Date", value=date.today())
day = match_date.day
month = match_date.month
year = match_date.year

# --- Prediction Logic ---
if st.button("Predict Score"):
    input_dict = {
        'runs': runs,
        'wickets': wickets,
        'overs': overs,
        'runs_last_5': runs_last_5,
        'wickets_last_5': wickets_last_5,
        'year': year,
        'month': month,
        'day': day
    }

    # Add one-hot encoding manually for teams
    for team in teams:
        input_dict[f'batting_team_{team}'] = 1 if team == batting_team else 0
        input_dict[f'bowling_team_{team}'] = 1 if team == bowling_team else 0

    # Create DataFrame
    input_df = pd.DataFrame([input_dict])

    # Reindex to match training features
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Predict
    predicted_score = int(model.predict(input_df)[0])

    st.success(f"🏏 Predicted Final Score for {batting_team}: {predicted_score} runs")

    # Add simple logic to show likely winner
    if predicted_score >= 170:
        st.markdown(f"🏆 **Likely Winner: {batting_team}** (High Score)")
    else:
        st.markdown(f"🔮 **Likely Winner: {bowling_team}** (Chasing Advantage)")
