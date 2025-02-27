import json
import time


def add_timestamp_to_vocabulary_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    for word in vocabulary:
        if "added_on" not in vocabulary[word]:
            timestamp = int(time.time())
            vocabulary[word]["added_on"] = timestamp

    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)


def add_adoption_to_vocabulary_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    for word in vocabulary:
        if "adoption" not in vocabulary[word]:
            vocabulary[word]["adoption"] = 0

    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    user_ids = [344989590, 391819710]
    for user_id in user_ids:
        vocabulary_file_name = f"../examples/{user_id}_vocabulary.json"
        add_timestamp_to_vocabulary_file(vocabulary_file_name)
        add_adoption_to_vocabulary_file(vocabulary_file_name)
