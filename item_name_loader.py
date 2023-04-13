import requests
import json

with open('csgo_skins.json', 'r', encoding='utf-8') as csgo_file:
    csgo_data = json.load(csgo_file)
    with open('csgo_item_list.json', 'w', encoding='utf-8') as f:
        for i in csgo_data["items_list"]:
            print(i, file=f)