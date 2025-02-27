import json
import time
import xml.etree.ElementTree as ET


def load_anki_vocabulary_to_daily_dragon_vocabulary(xml_file, json_file):
    """Load words from vocabulary extracted from ANKI in XML format to json format of daily-dragon."""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        raise ValueError(f"Invalid JSON file: {json_file}")

    tree = ET.parse(xml_file)
    root = tree.getroot()

    new_words = {}
    for card in root.findall(".//card"):
        word_element = card.find(".//chinese[@name='Chinese']")
        meaning_element = card.find(".//chinese[@name='Meaning']")

        if word_element is not None and meaning_element is not None:
            word = word_element.text.strip()
            translation = meaning_element.text.strip()

            if word in json_data:
                print(f"Skipping duplicate word: {word}")
            else:
                new_words[word] = {
                    "pronunciation": "",
                    "translation": translation,
                    "added_on": int(time.time()),
                    "adoption": 0
                }

    if new_words:
        json_data.update(new_words)
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        print(f"JSON updated successfully. Added {len(new_words)} new words: {list(new_words.keys())}")
    else:
        print("No new words added.")


anki_vocabulary = "C:\\Users\\Oleksandr_Gavryliuk\\Documents\\daily_dragon\\chinese.xml"
my_daily_dragon_vocabulary = "C:\\Users\\Oleksandr_Gavryliuk\\IdeaProjects\\daily-dragon\\examples\\344989590_vocabulary.json"
load_anki_vocabulary_to_daily_dragon_vocabulary(anki_vocabulary, my_daily_dragon_vocabulary)
