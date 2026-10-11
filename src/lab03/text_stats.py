import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    text = sys.stdin.read()
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()