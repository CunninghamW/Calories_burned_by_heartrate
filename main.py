from caloriecalculator import CalorieCalculator

def main():
    session = CalorieCalculator()

    session.get_sex()
    session.get_vo2()
    session.get_age()
    session.get_weight()
    session.get_exercise_duration()
    session.get_heart_rate()

    calories = session.calculate_calories()
    print(f"\nEstimated calories burned: {calories:.2f}")

if __name__ == "__main__":
        main()



