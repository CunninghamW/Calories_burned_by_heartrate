class CalorieCalculator:
    def __init__(self):
        self.user_sex = None
        self.user_age = None
        self.user_vo2 = None
        self.user_weight = None
        self.user_exercise_duration = None
        self.user_heart_rate = None


    def get_sex(self):
        self.user_sex = input("What is your sex? Male or Female?: " ).lower()
        
    def get_age(self):
        self.user_age = int(input("What is your age?: "))

    def get_vo2(self):
        vo2_known_unknown = input("Do you know your VO2 max? Yes or no?: ").lower()
        if vo2_known_unknown == "yes":
            self.user_vo2 = float(input("What is your VO2 max?: "))

        else:
            self.user_vo2 = None

    def get_weight(self):
        weight_lbs = float(input("What is your weight (lbs)?: "))
        self.user_weight = weight_lbs * 0.453592

    def get_exercise_duration(self):
        self.user_exercise_duration = int(input("How many minutes was your workout?: "))

    def get_heart_rate(self):
        self.user_heart_rate = int(input("What was your average heart rate?: "))

    def calculate_calories(self):
        if self.user_vo2 is None:
            if self.user_sex == "male":
                self.calories_burned = self.user_exercise_duration * (0.6309 * self.user_heart_rate 
                                                                      + 0.1988 * self.user_weight 
                                                                      + 0.2017 * self.user_age - 55.0969) / 4.184
            else:
                self.calories_burned = self.user_exercise_duration * (0.4472 * self.user_heart_rate 
                                                                      + 0.1263 * self.user_weight 
                                                                      + 0.074 * self.user_age - 20.4022) / 4.184
        else:
            if self.user_sex == "male":
                self.calories_burned = self.user_exercise_duration * (0.634 * self.user_heart_rate +
                                                                      0.404 * self.user_vo2
                                                                      + 0.1263 * self.user_weight 
                                                                      + 0.074 * self.user_age - 95.7735) / 4.184
            else:
                self.calories_burned = self.user_exercise_duration * (0.45 * self.user_heart_rate +
                                                                      0.380 * self.user_vo2
                                                                      + 0.103 * self.user_weight 
                                                                      + 0.274 * self.user_age - 593954) / 4.184

        return self.calories_burned


