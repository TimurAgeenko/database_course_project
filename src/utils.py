import json
import os


def save_data_to_file(filename, data: list, path: str = "../data/") -> None:
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + filename + ".json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
