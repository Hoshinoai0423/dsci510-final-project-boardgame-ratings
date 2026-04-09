import pandas as pd

def load_kaggle_data(file_path="E:\dsci510-final-project-boardgame-ratings/data/board_games.csv"):
    return pd.read_csv(file_path)