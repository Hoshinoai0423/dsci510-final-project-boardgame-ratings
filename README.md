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

At the current stage, the project has completed data loading and cleaning using the Kaggle dataset.

The dataset has been processed by:
- removing irrelevant columns (e.g., text and image fields)
- selecting numerical features
- preparing data for machine learning models

Further modeling (e.g., Decision Tree) will be implemented in the next stage.


# Installation

- Python 3.9+
- Required packages:

```bash
pip install -r requirements.txt
```

If using BoardGameGeek API in the future, a token may be required and stored in a .env file.

# Running analysis

1. Place the Kaggle dataset file `board_games.csv` in the `data/` folder.

2. Open Jupyter Notebook:

```bash
cd src
jupyter notebook
```

Open the notebook and run all cells to:
load the dataset
clean the data
prepare features for analysis

Note:

The current workflow is notebook-based.
API and HTML extraction scripts are included but not yet fully operational due to access limitations.














