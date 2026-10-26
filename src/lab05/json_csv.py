import csv
import json
from pathlib import Path
from src.lib.io_helpers import ensure_parent_dir

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """Преобразовывает JSON в CSV.

    Кодировка UTF-8. Отсутствующие поля заполняются пустой строкой.
    ValueError: неверное расширение файла; битый JSON; пустой JSON; в списке есть НЕ словарь.
    FileNotFoundError: JSON-файл не найден.
    """
    json_p = Path(json_path)
    csv_p = Path(csv_path)

    if not json_p.exists():
        raise FileNotFoundError(f'JSON файл не найден {json_p}')
    if json_p.suffix.lower() != ".json":
        raise ValueError("Ожидался файл с расширением .json")
    if csv_p.suffix.lower() != ".csv":
        raise ValueError("Ожидался файл с расширением .csv")

    with json_p.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Битый JSON: {e.msg}, строка {e.lineno}") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен быть списком словарей")

    fieldnames = []
    for item in data:
        for key in item:
            if key not in fieldnames:
                fieldnames.append(key)
    
    ensure_parent_dir(csv_p)
    with csv_p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """Преобразовывает CSV в JSON.
    
    ValueError: неверное расширение файла; CSV пустой или без заголовка; в CSV только заголовок.
    FileNotFoundError: CSV-файл не найден.
    """
    csv_p = Path(csv_path)
    json_p = Path(json_path)

    if not csv_p.exists():
        raise FileNotFoundError(f"CSV-файл не найден: {csv_p}")
    if csv_p.suffix.lower() != ".csv":
        raise ValueError("Ожидался файл с расширением .csv")
    if json_p.suffix.lower() != ".json":
        raise ValueError("Ожидался файл с расширением .json")

    with csv_p.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV пустой или без заголовка")
        rows = list(reader)

    if not rows:
        raise ValueError("В CSV нет данных, только заголовок")

    ensure_parent_dir(json_p)
    with json_p.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("Готово: результаты в data/out/")