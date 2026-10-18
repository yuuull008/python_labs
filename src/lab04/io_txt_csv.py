import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл целиком и возвращает его содержимое одной строкой.
    Чтобы прочитать файл в другой кодировке:
        read_text("data/input.txt", encoding="cp1251").
    FileNotFoundError: файл не найден.
    UnicodeDecodeError: содержимое не соответствует указанной кодировке.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создает/перезаписывает CSV-файл с разделителем ','.
    header: заголовок. Если передан, пишется первой строкой.
    ValueError: если строки в rows имеют разную длину.
    """
    rows = list(rows)
    if rows:
        width = len(rows[0])
        for row in rows:
            if len(row) != width:
                raise ValueError("все строки rows должны иметь одинаковую длину")
    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские папки для path, если их ещё нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)