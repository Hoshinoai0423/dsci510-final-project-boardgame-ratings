import os
import time
import requests
import xml.etree.ElementTree as ET
import pandas as pd
from dotenv import load_dotenv


load_dotenv()


def load_bgg_token() -> str:
    token = os.getenv("BGG_TOKEN")
    if not token:
        raise ValueError("BGG_TOKEN not found in .env file")
    return token


def _safe_get_value(parent, tag: str) -> str | None:
    child = parent.find(tag) if parent is not None else None
    return child.attrib.get("value") if child is not None else None


def chunk_list(items, chunk_size=20):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


def parse_item(item) -> dict:
    game_id = int(item.attrib.get("id"))

    # Get primary name
    name = None
    for name_tag in item.findall("name"):
        if name_tag.attrib.get("type") == "primary":
            name = name_tag.attrib.get("value")
            break

    if name is None:
        first_name = item.find("name")
        name = first_name.attrib.get("value") if first_name is not None else None

    # Basic fields
    yearpublished = _safe_get_value(item, "yearpublished")
    minplayers = _safe_get_value(item, "minplayers")
    maxplayers = _safe_get_value(item, "maxplayers")
    playingtime = _safe_get_value(item, "playingtime")
    minplaytime = _safe_get_value(item, "minplaytime")
    maxplaytime = _safe_get_value(item, "maxplaytime")
    minage = _safe_get_value(item, "minage")

    # Lists from link tags
    categories = []
    mechanics = []
    designers = []
    publishers = []

    for link in item.findall("link"):
        link_type = link.attrib.get("type")
        link_value = link.attrib.get("value")

        if link_type == "boardgamecategory":
            categories.append(link_value)
        elif link_type == "boardgamemechanic":
            mechanics.append(link_value)
        elif link_type == "boardgamedesigner":
            designers.append(link_value)
        elif link_type == "boardgamepublisher":
            publishers.append(link_value)

    # Statistics fields
    ratings = item.find("statistics/ratings")

    average = _safe_get_value(ratings, "average")
    usersrated = _safe_get_value(ratings, "usersrated")
    bayesaverage = _safe_get_value(ratings, "bayesaverage")
    stddev = _safe_get_value(ratings, "stddev")
    owned = _safe_get_value(ratings, "owned")
    trading = _safe_get_value(ratings, "trading")
    wanting = _safe_get_value(ratings, "wanting")
    wishing = _safe_get_value(ratings, "wishing")
    numcomments = _safe_get_value(ratings, "numcomments")
    numweights = _safe_get_value(ratings, "numweights")
    averageweight = _safe_get_value(ratings, "averageweight")

    return {
        "id": game_id,
        "name": name,
        "yearpublished": yearpublished,
        "minplayers": minplayers,
        "maxplayers": maxplayers,
        "playingtime": playingtime,
        "minplaytime": minplaytime,
        "maxplaytime": maxplaytime,
        "minage": minage,
        "categories": categories,
        "mechanics": mechanics,
        "designers": designers,
        "publishers": publishers,
        "average": average,
        "usersrated": usersrated,
        "bayesaverage": bayesaverage,
        "stddev": stddev,
        "owned": owned,
        "trading": trading,
        "wanting": wanting,
        "wishing": wishing,
        "numcomments": numcomments,
        "numweights": numweights,
        "averageweight": averageweight
    }


def get_game_details(game_id: int, token: str) -> dict:
    url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}&stats=1"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    item = root.find("item")

    if item is None:
        raise ValueError(f"No game found for game id: {game_id}")

    return parse_item(item)


def get_games_details_batch(batch_ids: list[int], token: str) -> list[dict]:
    ids_str = ",".join(map(str, batch_ids))
    url = f"https://boardgamegeek.com/xmlapi2/thing?id={ids_str}&stats=1"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    items = root.findall("item")

    if not items:
        raise ValueError(f"No games found for batch ids: {batch_ids}")

    games_data = []
    for item in items:
        try:
            games_data.append(parse_item(item))
        except Exception as e:
            print(f"Error parsing item {item.attrib.get('id')}: {e}")

    return games_data


def fetch_games_from_list(game_ids: list[int]) -> pd.DataFrame:
    token = load_bgg_token()
    games_data = []

    for batch_ids in chunk_list(game_ids, 20):
        try:
            batch_data = get_games_details_batch(batch_ids, token)
            games_data.extend(batch_data)

            print(f"Fetched batch: {batch_ids}")

            # Wait between batch requests
            time.sleep(5)

        except Exception as e:
            print(f"Skipping batch {batch_ids}: {e}")
            time.sleep(10)

    return pd.DataFrame(games_data)