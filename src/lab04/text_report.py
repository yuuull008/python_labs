import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lab04.io_txt_csv import ensure_parent_dir, read_text, write_csv
from lib.text import count_freq, normalize, tokenize, top_n

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Возвращает пары (слово, частота): по убыванию частоты, при равенстве по слову."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def parse_args():
    """
    --in: входной текстовый файл.
    --out: путь к CSV-отчёту.
    --encoding: кодировка входного файла.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="in_path", default="data/input.txt")
    parser.add_argument("--out", dest="out_path", default="data/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    return parser.parse_args()

def main() -> None:
    """Читает файл, считает частоты, сохраняет CSV и печататет сводку."""
    args = parse_args()
    text = read_text(args.in_path, encoding=args.encoding)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    rows = sorted_word_counts(freq)
    ensure_parent_dir(args.out_path)
    write_csv(rows, args.out_path, header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()