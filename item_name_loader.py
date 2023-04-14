import json
import os
from config import weapons

weapons = ['AK-47', 'AWP', 'AUG', 'CZ75-Auto', 'Desert Eagle', 'Dual Berrettas', 'FAMAS', 'Five-SeveN', 'G3SG1', 'Galil AR', 'Glock-18',
           'M4A1-S', 'M4A4', 'M249', 'MAC-10', 'MAG-7', 'MP5-SD', 'MP7', 'MP9', 'Negev', 'Nova', 'P90', 'P250', 'P2000', 'PP-Bizon',
           'R8 Revolver', 'Sawed-Off', 'SCAR-20', 'SG 553', 'SSG 08', 'Tec-9', 'UMP-45', 'USP-S', 'XM1014']

def read_csgo_skins():
    with open('csgo_skins.json', 'r', encoding='utf-8') as csgo_file:
        csgo_data = json.load(csgo_file)
        with open('csgo_item_list.json', 'w', encoding='utf-8') as f:
            for i in csgo_data["items_list"]:
                print(i, file=f)

def sort_cs_weapons():
    print(os.getcwd())
    with open('csgo_item_list.txt', 'r', encoding='utf-8') as csgo_file:
        lines = csgo_file.readlines()

    if csgo_file is None:
        return
     
    os.chdir('Item_Name_Data')
    os.chdir('Weapons')
    
    for weapon in weapons:
        with open(weapon + '.txt', 'w', encoding='utf-8') as f:
            for line in lines:
                if weapon in line and 'Sticker' not in line and 'Graffiti' not in line:
                    print(line.strip(), file=f)


if __name__ == "__main__":
    sort_cs_weapons()
