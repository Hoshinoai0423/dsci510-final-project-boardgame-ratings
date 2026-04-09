import requests
import pandas as pd
from bs4 import BeautifulSoup


def fetch_ranking_page_html(page: int = 1) -> str:
    if page == 1:
        url = "https://boardgamegeek.com/browse/boardgame"
    else:
        url = f"https://boardgamegeek.com/browse/boardgame/page/{page}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=20)

    if response.status_code == 403:
        raise PermissionError(
            "BoardGameGeek ranking page returned 403 Forbidden. "
            "Direct scripted HTML access is currently blocked."
        )

    response.raise_for_status()
    return response.text


def parse_ranking_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    data = []

    rows = soup.select("tr[id^='row_']")

    for row in rows:
        rank_tag = row.select_one(".collection_rank")
        name_tag = row.select_one(".primary")
        rating_tags = row.select(".collection_bggrating")
        voters_tag = row.select_one(".collection_numowners")

        rank = rank_tag.get_text(strip=True) if rank_tag else None
        name = name_tag.get_text(strip=True) if name_tag else None
        geek_rating = rating_tags[0].get_text(strip=True) if len(rating_tags) >= 1 else None
        avg_rating = rating_tags[1].get_text(strip=True) if len(rating_tags) >= 2 else None
        num_voters = voters_tag.get_text(strip=True) if voters_tag else None

        game_id = None
        if name_tag and name_tag.has_attr("href"):
            parts = name_tag["href"].split("/")
            if len(parts) > 2:
                game_id = parts[2]

        data.append({
            "id": game_id,
            "rank": rank,
            "name": name,
            "geek_rating": geek_rating,
            "avg_rating": avg_rating,
            "num_voters": num_voters
        })

    return data


def scrape_rankings(pages: int = 1) -> pd.DataFrame:
    all_data = []

    for page in range(1, pages + 1):
        html = fetch_ranking_page_html(page)
        page_data = parse_ranking_html(html)
        all_data.extend(page_data)

    return pd.DataFrame(all_data)