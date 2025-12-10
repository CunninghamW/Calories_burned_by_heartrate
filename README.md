# Calories Burned from Heart Rate Calculator

An interactive Streamlit web application that estimates calories burned during
a workout using heart rate–based formulas. The app collects user metrics such as age, sex, weight, workout duration, and average heart rate, with optional VO₂ max support, to calculate calorie expenditure.

---

## Features
- Estimates calories burned during validated physiological formulas
- Supports calculations **with or without V02 max**
- Interactive web interface built with Streamlit
- Accepts weight in pounds and converts internally to kilograms for accuracy
- Clean, modular, object-oriented Python design
- User-friendly input validation via Streamlit controls

---

## How It Works
The calculator uses heart rate-based equations to estimate energy expenditure:

- Inputs:
    - Sex
    - Age
    - Weight (lbs, converted to kg internally)
    - Workout duration (minutes)
    - Average heart rate (bpm)
    - Optional VO2 max

- The app selects the appropriate formula based on sex and VO2 availabilty and
  returns estimated calories burned (kcal).

## Tech Stack
- **Python**
- **Streamlit**
- Object-Oriented Programming

---

## Running the App Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/CunninghamW/Calories_burned_by_heartrate.git 
    cd Calories_burned_by_heartrate

2. Install dependencies:
    pip install -r requirments.txt

3. Run the Streamlit app:
    streamlit run app.py

## Notes
- This application provides estimates, not medical advice.
- Accuracy depends on correct input values and consistent heart rate measurement.
