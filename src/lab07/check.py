import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100) -> int:
    """Сравнивает fn(nums) с sorted(nums) и проверяет, что исходный список цел.
    Возвращает число проведённых проверок.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {original}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список: было {original}, стало {nums}"
    return trials


def check_search() -> int:
    """Сравнивает linear_search с list.index, а binary_search проверяет по содержимому.
    Возвращает число проведённых проверок.
    """
    checks = 0
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        sorted_nums = sorted(nums)
        targets = [101]
        if nums:
            targets += [nums[0], nums[-1], random.choice(nums)]

        for x in targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            got = linear_search(nums, x)
            assert got == expected, f"linear_search({nums}, {x}) = {got}, ожидали {expected}"

            got = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert 0 <= got < len(sorted_nums), f"binary_search({sorted_nums}, {x}) вернул {got}"
                assert sorted_nums[got] == x, f"binary_search({sorted_nums}, {x}) = {got}, а там не x"
            else:
                assert got == -1, f"binary_search({sorted_nums}, {x}) = {got}, ожидали -1"
            checks += 1
    return checks


def check_two_sum(trials=100) -> int:
    """Оба two_sum должны вернуть одну из подходящих пар, а если пар нет, то None.
    Возвращает число проведённых проверок.
    """
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)
        expected = []
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    expected.append((i, j))

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        info = f"nums={nums}, target={target}, brute={brute}, fast={fast}"
        if expected:
            assert brute in expected, "two_sum_brute вернул неверную пару: " + info
            assert fast in expected, "two_sum_fast вернул неверную пару: " + info
        else:
            assert brute is None, "two_sum_brute нашёл пару, которой нет: " + info
            assert fast is None, "two_sum_fast нашёл пару, которой нет: " + info
    return trials


if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок пройдено")