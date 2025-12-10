import streamlit as st
from caloriecalculator import CalorieCalculator

# Title of the app

st.title("Calories Burned from Heart Rate Calculator")

# Short description 
st.markdown("""
This app estimates the calories you burned during a workout based on your **average heart rate**, **duration**, and **weight**.  
You can also enter your VO2 max if known, but it is optional.
""")

# Create a new session
st.sidebar.header("Your Workout Info")
session = CalorieCalculator()

# user inputs
session.user_sex = st.sidebar.selectbox("Sex", ["male", "female"])
session.user_age = st.sidebar.number_input("Age", min_value=10, max_value=120, value=25)
weight_lbs = st.sidebar.number_input("Weight (lbs)", min_value=10, max_value=1000, value=70)
session.user_weight = weight_lbs * 0.453592
session.user_exercise_duration = st.sidebar.number_input("Workout duration (minutes)", min_value=1, max_value=300, value=30)
session.user_heart_rate = st.sidebar.number_input("Average heart rate (bpm)", min_value=40, max_value=220, value=120)

# VO2 max input 
vo2_known = st.sidebar.radio("Do you know your VO2 max?", ["Yes", "No"])
if vo2_known == "Yes":
    session.user_vo2 = st.sidebar.number_input("VO2 max", min_value=10.0, max_value=100.0, value=40.0)
else:
    session.user_vo2 = None 


# Calculate calories when the button is clicked
if st.button("Calculate Calories Burned"):
    calories = session.calculate_calories()
    st.success(f"Estimated calories burned: {calories:.2f} kcal")

    # calories burned per minute
    calories_per_min = calories / session.user_exercise_duration
    st.info(f"Calories burned per minute: {calories_per_min:.2f} kcal/min")
                     