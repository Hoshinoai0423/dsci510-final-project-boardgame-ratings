from pathlib import Path

# Base directories
SRC_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SRC_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"

# Data source URLs
BGG_API_URL = "https://boardgamegeek.com/xmlapi2/thing"
BGG_RANKS_URL = "https://boardgamegeek.com/data_dumps/bg_ranks"

# Input file names
BGG_RANKS_FILE = DATA_DIR / "boardgames_ranks.csv"

# Output data files
FINAL_DATA_FILE = DATA_DIR / "final_top500_games.csv"

# Output result files
RMSE_PLOT_FILE = RESULTS_DIR / "rmse_vs_depth.png"
R2_PLOT_FILE = RESULTS_DIR / "r2_vs_depth.png"
MODEL_SUMMARY_FILE = RESULTS_DIR / "model_summary.csv"
FEATURE_IMPORTANCE_FILE = RESULTS_DIR / "feature_importance.csv"