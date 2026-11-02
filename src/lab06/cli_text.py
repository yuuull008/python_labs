import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text


def cat_command(input_path: str, numbered: bool = False) -> None:
    path = Path(input_path)
    if not path.is_file():
        raise FileNotFoundError("Файл не найден")

    with open(path, "r", encoding="utf-8") as f:
        for num, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if numbered:
                print(f"{num}: {line}")
            else:
                print(line)


def stats_command(input_path: str, top: int = 5) -> None:
    path = Path(input_path)
    if not path.is_file():
        raise FileNotFoundError("Файл не найден")

    text = read_text(input_path)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести файл построчно")
    cat_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Размер топа (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть больше 0")

    try:
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)
    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")
    except UnicodeDecodeError:
        parser.error(f"Файл {args.input} не в кодировке UTF-8")


if __name__ == "__main__":
    main()