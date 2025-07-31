import pandas as pd
import os

class GroupData:
    def __init__(self, df, config_data, output_dir=None):
        """
        :param df: The preprocessed or engineered dataframe
        :param config_path: Path to Excel file with grouping configurations
        :param output_dir: Optional directory to save each profile as a CSV
        """
        self.df = df.copy()
        self.config_data = config_data
        self.output_dir = "E:\personal\data"
        self.grouped_profiles = {}

        # Create output directory if needed
        os.makedirs(self.output_dir, exist_ok=True)

    def group_data(self):
        """
        Read config file and perform grouping based on each row in the 'group_by' column.
        Save each grouped DataFrame in self.grouped_profiles and optionally write to CSV.
        """
        config_df = self.config_data

        if 'group_by' not in config_df.columns:
            raise ValueError("Configuration file must contain a 'group_by' column.")

        for i, row in config_df.iterrows():
            group_by_cols = [col.strip() for col in row['group_by'].split(',')]
            print("group by col: ", group_by_cols)

            group_name = "_".join(group_by_cols)
            grouped = self.df.groupby(group_by_cols)['amount'].agg(['sum', 'mean', 'count']).reset_index()
            self.grouped_profiles[group_name] = grouped

            # Optionally save to CSV
            output_file = os.path.join(self.output_dir, f"group_{group_name}.csv")
            grouped.to_csv(output_file, index=False)

        return self.grouped_profiles
