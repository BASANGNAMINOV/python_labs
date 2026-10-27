import csv 
import json
from pathlib import Path

from src.lib.io_txt_csv import read_text
from src.lib.io_txt_csv import write_csv

def check_ext(file_path: str, ext: str) -> None:
    """Проверяет расширение файла."""
    if Path(file_path).suffix.lower() != ext:
        raise ValueError("Неверное расширение файла")


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей, заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8.
    """
    check_ext(json_path, ".json")
    check_ext(csv_path, ".csv")

    data = read_text(json_path)

    if not data.strip():
        raise ValueError("JSON-файл пустой или содержит неподдерживаемые данные")

    records = json.loads(data)

    if not isinstance(records, list) or not records:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Каждый элемент JSON должен быть словарём")

    headers = []

    for record in records:
        for key in record:
            if key not in headers:
                headers.append(key)

    if not headers:
        raise ValueError("В JSON отсутствуют данные для записи")

    rows = []

    for record in records:
        row = []

        for header in headers:
            row.append(record.get(header, ""))

        rows.append(row)

    write_csv(rows, csv_path, header=tuple(headers))


def csv_to_json(csv_path: str, json_path: str) -> None:
    
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """

    check_ext(csv_path, ".csv")
    check_ext(json_path, ".json")

    with open(csv_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, restval="")

        if not reader.fieldnames:
            raise ValueError("CSV-файл не содержит заголовков")

        records = list(reader)

    if not records:
        raise ValueError("В CSV-файле нет строк с данными")

    output = Path(json_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")