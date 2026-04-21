import pandas as pd
from bgg_api import fetch_games_from_list


def test_fetch_fixed_ids():
    test_ids = [1, 2, 3, 4, 5]

    print("Testing API with fixed IDs:", test_ids)
    bgg_df = fetch_games_from_list(test_ids)

    print("\nFetched BGG data:")
    print(bgg_df)

    return bgg_df


def test_compare_with_kaggle():
    csv_path = "E:/dsci510-final-project-boardgame-ratings/data/board_games.csv"
    kaggle_df = pd.read_csv(csv_path)

    sample_ids = [1, 2, 3, 4, 5]

    kaggle_subset = kaggle_df[kaggle_df["game_id"].isin(sample_ids)].copy()
    bgg_df = fetch_games_from_list(sample_ids)

    print("\nKaggle subset:")
    print(kaggle_subset[["game_id", "name"]])

    print("\nBGG subset:")
    print(bgg_df[["id", "name"]])

    return kaggle_subset, bgg_df