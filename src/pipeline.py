import pandas as pd
from src.preprocessing import Preprocessing
from src.group_data import GroupData
from src.feature_engineering import FeatureEngineering

def run():
    data = pd.read_csv("E:/personal/Mlops/data/transactions.csv")
    pp_obj = Preprocessing(data)
    pp_obj.preprocess()
    fe_obj = FeatureEngineering(pp_obj.df)
    fe_obj.feature_engineering()
    config = pd.DataFrame({"group_by": ["sender_bank",
                                        "sender_location",
                                        "benefi_bank",
                                        "benefi_country",
                                        "sender_bank,benefi_bank",
                                        "sender_bank,benefi_country",
                                        "sender_bank,day_category",
                                        "sender_bank,time_category"]})
    group_obj = GroupData(fe_obj.df, config)
    data  = group_obj.group_data()
    print(data)

run()