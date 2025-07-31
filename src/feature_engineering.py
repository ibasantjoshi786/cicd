import pandas as pd

class FeatureEngineering:
    def __init__(self, df):
        """
        Initialize with a DataFrame that includes 'day' and 'hour' columns.
        """
        self.df = df.copy()

    def feature_engineering(self):
        """
        Apply all feature engineering transformations and return the updated DataFrame.
        """
        self.day_feature()
        self.time_feature()
        return self.df

    def day_feature(self):
        """
        Convert the 'day' column to a categorical feature:
        - 'start_of_month' for days 1–10
        - 'mid_of_month' for days 11–20
        - 'end_of_month' for days 21–31
        """
        def categorize_day(day):
            if day <= 10:
                return "start_of_month"
            elif day <= 20:
                return "mid_of_month"
            else:
                return "end_of_month"

        self.df['day_category'] = self.df['day'].apply(categorize_day)

    def time_feature(self):
        """
        Convert the 'hour' column into categorical time ranges:
        - early_morning: 4–7
        - morning: 8–11
        - afternoon: 12–15
        - evening: 16–19
        - night: 20–3
        """
        def categorize_time(hour):
            if 4 <= hour <= 7:
                return "early_morning"
            elif 8 <= hour <= 11:
                return "morning"
            elif 12 <= hour <= 15:
                return "afternoon"
            elif 16 <= hour <= 19:
                return "evening"
            else:
                return "night"

        self.df['time_category'] = self.df['hour'].apply(categorize_time)
