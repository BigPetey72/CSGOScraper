import json
import os

def read_csgo_skins():
    with open('csgo_skins.json', 'r', encoding='utf-8') as csgo_file:
        csgo_data = json.load(csgo_file)
        with open('csgo_item_list.json', 'w', encoding='utf-8') as f:
            for i in csgo_data["items_list"]:
                print(i, file=f)

def sort_cs_weapons():
    path = '/'
    
    with open('csgo_skins.json', 'r', encoding='utf-8') as csgo_file:
        csgo_data = json.load(csgo_file)

    os.chdir('Item_Name_Data')
    os.chdir('Weapons')
    files = os.listdir(os.getcwd())
    print(files)

if __name__ == "__main__":
    sort_cs_weapons()
