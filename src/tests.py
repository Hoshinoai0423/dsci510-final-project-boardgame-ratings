from kaggle_csv import load_kaggle_data

def test_load():
    df = load_kaggle_data()
    assert len(df) > 0