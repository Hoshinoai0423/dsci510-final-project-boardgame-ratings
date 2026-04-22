# Board Game Ratings Analysis

This project analyzes factors that influence board game ratings using machine learning techniques. The goal is to understand how features such as playtime, player count, and complexity relate to user ratings.


# Data sources

- **BoardGameGeek Ranking Dataset**
  
  https://boardgamegeek.com/data_dumps/bg_ranks
  
  An official dataset containing board game rankings, average ratings, and user statistics.  
  This dataset is used to identify the top 500 board games for analysis.

- **BoardGameGeek XML API**

  https://boardgamegeek.com
  
  Used to retrieve detailed game information, including mechanics, categories, player count, playtime, and complexity.  
  This serves as the primary source of features for the machine learning model.

- **Kaggle Dataset**

  https://www.kaggle.com/datasets/sujaykapadnis/board-games

  A dataset derived from the BoardGameGeek API, containing board game attributes and rating-related information.  
  Used for initial exploration to understand the structure of board game data.


# Results

The project successfully constructed a machine learning pipeline to analyze board game ratings using data from BoardGameGeek.

A decision tree regression model was trained to predict game ratings based on design-related features, including mechanics, categories, player count, playtime, and complexity.

Model performance was evaluated using RMSE and R² metrics:
- **Best model:**
  - max depth = 4
  - RMSE ≈ 0.217
  - R² ≈ 0.57

Hyperparameter tuning showed that a shallow tree (depth = 4) achieved the best balance between underfitting and overfitting.

Feature importance analysis indicates that:
- Game complexity (averageweight) and player-related attributes have a moderate impact on ratings
- Mechanics such as "Push Your Luck" show high influence on rating prediction.
- Popularity-related features were intentionally excluded to focus on design factors

Overall, the model explains a substantial portion of rating variation while maintaining interpretability.

# Installation

- Python 3.9+
- Required packages:

```bash
pip install -r requirements.txt
```

- Create a .env file in the src/ directory and add your BoardGameGeek API token:

```bash
BGG_TOKEN=your_token_here
```

Make sure the token is valid and API access has been approved.

# Running analysis

1. Download the BGG ranking dataset and place the extracted CSV file (e.g., `boardgames_ranks.csv`) in the `data/` folder:

- https://boardgamegeek.com/data_dumps/bg_ranks

2. Create a `.env` file in the `src/` directory and add your BGG API token:

```text
BGG_TOKEN=your_token_here
```



<img width="1104" height="324" alt="powered_by_BGG" src="https://github.com/user-attachments/assets/4df5e3ce-2ad3-4b3c-b520-e5af8f116354" />














