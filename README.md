# Board Game Ratings Analysis

This project analyzes factors that influence board game ratings using machine learning techniques. The goal is to understand how features such as playtime, player count, and complexity relate to user ratings.


# Data sources

- **Kaggle Dataset**  
  A dataset containing board game attributes such as player counts, playtime, minimum age, year published, and user ratings.  
  This is the primary data source currently used in the project.

- **BoardGameGeek XML API (planned)**  
  Intended for retrieving additional game details. API access has been requested and is pending approval.

- **BoardGameGeek HTML pages (planned)**  
  Attempted to scrape ranking data, but direct access is currently restricted (HTTP 403).


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














