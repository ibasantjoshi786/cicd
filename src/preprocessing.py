import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


class Preprocessing:

    def __init__(self, df):
        """
        Initialize with the dataframe
        """
        self.df = df.copy()
        self.preprocessor = None

    def preprocess(self):
        """
        Runs the full preprocessing pipeline
        """
        # Convert date and time to datetime
        self.df['datetime'] = pd.to_datetime(self.df['date'].astype(str) + ' ' + self.df['time'].astype(str))

        # Extract date and time features
        self.extract_date()
        self.extract_time()

        # Convert amount float to int (e.g. in cents) if needed
        self.convert_float_to_int()

        # Drop original date and time columns after extraction
        self.df.drop(['date', 'time'], axis=1, inplace=True)

        # Define categorical and numerical columns for transformation
        cat_cols = ['sender_bank', 'sender_location', 'benefi_bank', 'benefi_country']
        num_cols = ['amount', 'hour', 'day', 'month', 'year', 'quarter']

        # Create ColumnTransformer with scaling and encoding
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), num_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
            ])

        # Fit and transform the data
        processed = self.preprocessor.fit_transform(self.df)

        return processed

    def extract_date(self):
        """
        Extract day, year, month, quarter from datetime column
        """
        self.df['day'] = self.df['datetime'].dt.day
        self.df['month'] = self.df['datetime'].dt.month
        self.df['year'] = self.df['datetime'].dt.year
        self.df['quarter'] = self.df['datetime'].dt.quarter

    def extract_time(self):
        """
        Extract hour from datetime column in 24 hour format
        """
        self.df['hour'] = self.df['datetime'].dt.hour


    def convert_float_to_int(self):
        """
        Convert amount float to integer cents (optional for modeling)
        """
        self.df['amount'] = (self.df['amount']).astype(int)
