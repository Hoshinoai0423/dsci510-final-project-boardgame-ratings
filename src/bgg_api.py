import requests
import xml.etree.ElementTree as ET
import pandas as pd


def load_bgg_token(filename: str = "bgg_token.txt") -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()


def get_game_details(game_id: int, token: str) -> dict:
    url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}"

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

    name_tag = item.find("name")
    name = name_tag.attrib.get("value") if name_tag is not None else None

    minplayers = item.find("minplayers").attrib.get("value") if item.find("minplayers") is not None else None
    maxplayers = item.find("maxplayers").attrib.get("value") if item.find("maxplayers") is not None else None
    playingtime = item.find("playingtime").attrib.get("value") if item.find("playingtime") is not None else None

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

    return {
        "id": game_id,
        "name": name,
        "minplayers": minplayers,
        "maxplayers": maxplayers,
        "playingtime": playingtime,
        "categories": categories,
        "mechanics": mechanics,
        "designers": designers,
        "publishers": publishers
    }


def fetch_games_from_list(game_ids: list[int], token_file: str = "bgg_token.txt") -> pd.DataFrame:
    token = load_bgg_token(token_file)
    games_data = []

    for game_id in game_ids:
        try:
            game_info = get_game_details(game_id, token)
            games_data.append(game_info)
        except Exception as e:
            print(f"Skipping game id {game_id}: {e}")

    return pd.DataFrame(games_data)