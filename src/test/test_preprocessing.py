import pandas as pd
import pytest
from src.pipeline import Preprocessing

@pytest.fixture(scope="module")
def setup_db():
    data_object = pd.DataFrame({
        "sender_acc_no": ["Acc1", "Acc1", "Acc2", "Acc2", "Acc1", "Acc2"],
        "sender_bank": ["Bank1", "Bank2", "Bank2", "Bank2", "Bank1", "Bank1"],
        "sender_location": ["India", "India", "US", "US", "US", "US"],
        "benefi_acc_no": ["Ben1", "Ben1", "Ben2", "Ben2", "Ben2", "Ben1"],
        "benefi_bank": ["Bank1", "Bank2", "Bank2", "Bank2", "Bank1", "Bank1"],
        "benefi_country": ["Dubai", "India", "US", "US", "US", "Dubai"],
        "date": ["2/1/2025", "10/1/2025", "2/1/2025", "10/3/2025", "2/2/2025", "10/9/2025"],
        "time": ["13:00", "11:00", "09:00", "8:00", "23:00", "12:00"],
        "amount": [100.98, 200, 300, 400, 500, 600]
    })

    data_object['date'] = pd.to_datetime(data_object['date']).dt.strftime('%m/%d/%Y')

    data_object['time'] = pd.to_datetime(data_object['time'], format='%H:%M').dt.strftime('%I:%M:%S %p')
    pp_obj = Preprocessing(data_object)
    return pp_obj


def test_extract_date(setup_db):
    setup_db.df['datetime'] = pd.to_datetime(setup_db.df['date'] + ' ' + setup_db.df['time'])
    setup_db.extract_date()

    assert 'day' in setup_db.df.columns
    assert 'month' in setup_db.df.columns
    assert 'year' in setup_db.df.columns
    assert 'quarter' in setup_db.df.columns

    assert setup_db.df.loc[0, 'month'] == 2

def test_extract_time(setup_db):
    setup_db.df['datetime'] = pd.to_datetime(setup_db.df['date'] + ' ' + setup_db.df['time'])
    setup_db.extract_time()

    assert 'hour' in setup_db.df.columns
    assert setup_db.df.loc[0, 'hour'] == 13

def test_convert_float_to_int(setup_db):
    setup_db.convert_float_to_int()

    assert setup_db.df.loc[0, 'amount'] == 1100

