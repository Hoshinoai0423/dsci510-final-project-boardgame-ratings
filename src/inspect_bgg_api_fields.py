import os
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

load_dotenv()

def inspect_bgg_item(game_id: int):
    token = os.getenv("BGG_TOKEN")
    url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}&stats=1"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    item = root.find("item")

    print("Top-level child tags under <item>:")
    for child in item:
        print(child.tag, child.attrib)

    ratings = item.find("statistics/ratings")
    if ratings is not None:
        print("\nChild tags under <statistics>/<ratings>:")
        for child in ratings:
            print(child.tag, child.attrib)

inspect_bgg_item(1)