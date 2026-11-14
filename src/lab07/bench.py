import os
import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

CSV_PATH = "data/lab07/bench.csv"


def bench_sorts() -> list[tuple[str, int, str, str]]:
    """Замеряет sorted и три свои сортировки, возвращает список кортежей."""
    random.seed(42)
    rows = []
    sizes = [1_000, 10_000, 100_000]
    funcs = [
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ]
    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        time_s = timeit.timeit(lambda: sorted(data), number=10) / 10
        rows.append(("sorting", n, "sorted", f"{time_s:.6f}"))

        for name, fc in funcs:
            if n <= 10_000:
                if n == 1_000:  
                    assert fc(data) == sorted(data), f"{name} ошиблась на n={n}"
                time_s = timeit.timeit(lambda: fc(data), number=1)
                rows.append(("sorting", n, name, f"{time_s:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows


def bench_search() -> list[tuple[str, int, str, str]]:
    """Замеряет поиск (линейный и бинарный) и два решения Two Sum, возвращает список кортежей."""
    random.seed(42)
    rows = []
    n = 100_000
    data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
    targets = [random.choice(data) for _ in range(10_000)]  

    time_ls = timeit.timeit(lambda: [linear_search(data, t) for t in targets], number=1)
    rows.append(("search", n, "linear_search", f"{time_ls:.6f}"))

    time_sort = timeit.timeit(lambda: sorted(data), number=10) / 10
    rows.append(("search", n, "sort_for_binary", f"{time_sort:.6f}"))

    sorted_data = sorted(data)
    time_bs = timeit.timeit(lambda: [binary_search(sorted_data, t) for t in targets], number=5) / 5
    rows.append(("search", n, "binary_search", f"{time_bs:.6f}"))

    for size in [1_000, 10_000]:
        data_ts = [random.randint(0, 10**9) for _ in range(size)]
        target = data_ts[-2] + data_ts[-1]
        assert two_sum_brute(data_ts, target) is not None
        assert two_sum_fast(data_ts, target) is not None

        time_b = timeit.timeit(lambda: two_sum_brute(data_ts, target), number=1)
        rows.append(("two_sum", size, "two_sum_brute", f"{time_b:.6f}"))
        time_f = timeit.timeit(lambda: two_sum_fast(data_ts, target), number=100) / 100
        rows.append(("two_sum", size, "two_sum_fast", f"{time_f:.6f}"))
    return rows


def main():
    """Собирает все замеры, сохраняет в CSV и печатает таблицу в консоль."""
    header = ("task", "n", "impl", "seconds")
    rows = []
    rows.extend(bench_sorts())
    rows.extend(bench_search())

    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    write_csv(rows, CSV_PATH, header)

    print("Результаты бенчмарка:")
    print(f"{'Task':<10} | {'N':<8} | {'Impl':<18} | {'Seconds':<12}")
    print("-" * 56)
    for task, n, impl, sec in rows:
        print(f"{task:<10} | {n:<8} | {impl:<18} | {sec:<12}")
    print(f"Результаты сохранены в {CSV_PATH}")


if __name__ == "__main__":
    main()