import requests
from bs4 import BeautifulSoup
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "items_minified.db")

def process_character(char_name):
    char_url = f"https://perkycrewserver.com/charbrowser/index.php?page=character&char={char_name}"
    response = requests.get(char_url)

    if response.status_code != 200 or "character not found" in response.text.lower():
        return {"error": "Character not found"}

    # TODO: Parse HTML for class and equipment (placeholder)
    soup = BeautifulSoup(response.text, "html.parser")
    character_class = "Shadow Knight"
    equipment = {"Chest": "Old Chainmail"}

    class_token = normalize_class(character_class)
    if not class_token:
        return {"error": f"Unknown class: {character_class}"}

    upgrades = find_upgrades(class_token, equipment)
    return {"upgrades": upgrades, "errors": []}

def normalize_class(raw_class):
    mapping = {
        "Shadow Knight": "SK",
        "Cleric": "CLR",
        "Warrior": "WAR",
        # Add the rest as needed
    }
    return mapping.get(raw_class)

def find_upgrades(class_token, equipment):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, slot FROM items WHERE classes LIKE ?", (f"%{class_token}%",))
    rows = cursor.fetchall()
    conn.close()

    upgrades = []
    for row in rows[:3]:  # Limit for now
        item_id, name, slot = row
        upgrades.append({
            "itemName": name,
            "slot": slot,
            "reason": "Potential upgrade",
            "link": f"https://perkycrewserver.com/?a=item&id={item_id}"
        })
    return upgrades