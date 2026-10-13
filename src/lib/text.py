import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Функция приводит текст к единому размеру, превращает ё/Ё в е/Е и убирает лишние пробелы.
    Тесты: 
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    """
    if casefold:
        text=text.casefold()
    else:
        text=text.lower()
    if yo2e:
        text=text.replace('ё','е').replace("Ё", "Е")
    text=text.strip()
    text=' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    """Разбивает на «слова», числа и дефисные конструкции считает словами.
    Тесты:
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    """
    text=re.findall(r"\w+(?:-\w+)*", text)
    return text

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоты слов и возвращает словарь с ними.
    Тест:
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    """
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N самых частых слов и сортирует их по убыванию/алфавиту.
    Тесты:
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    """
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:n]
