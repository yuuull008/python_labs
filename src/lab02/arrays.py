def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает кортеж (минимум, максимум). Пустой список - ValueError"""
    if len(nums)==0:
        raise ValueError('Список пуст')
    minimum=nums[0]
    maximum=nums[0]
    for i in nums:
        if i<minimum:
            minimum=i
        if i>maximum:
            maximum=i
    return(minimum,maximum)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений (по возрастанию)"""
    unique=[]
    c=0
    for x in nums:
        if x not in unique:
            unique.append(x)
    for i in range(len(unique)):
        for j in range(len(unique) - 1 - i):
            if unique[j]>unique[j+1]:
                c=unique[j]
                unique[j]=unique[j+1]
                unique[j+1]=c
    return(unique)


def flatten(mat: list[list | tuple]) -> list:
    """«Расплющивает» список списков/кортежей в один список по строкам"""
    res=[]
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Строка должна быть списком или кортежем")
        for x in row:
            res.append(x)
    return res

#тест-кейсы
print('min_max([3, -1, 5, 5, 0]) ->', min_max([3, -1, 5, 5, 0]))
print('min_max([42]) ->', min_max([42]))
print('min_max([-5, -2, -9]) ->', min_max([-5, -2, -9]))
print('min_max([1.5, 2, 2.0, -3.1]) ->', min_max([1.5, 2, 2.0, -3.1]))

try:
    print('min_max([]) ->', min_max([]))
except ValueError as error:
    print(f'min_max([]) -> ValueError: {error}')


print('unique_sorted([3, 1, 2, 1, 3]) ->', unique_sorted([3, 1, 2, 1, 3]))
print('unique_sorted([]) ->', unique_sorted([]))
print('unique_sorted([-1, -1, 0, 2, 2]) ->', unique_sorted([-1, -1, 0, 2, 2]))
print('unique_sorted([1.0, 1, 2.5, 2.5, 0]) ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))


print('flatten([[1, 2], [3, 4]]) ->', flatten([[1, 2], [3, 4]]))
print('flatten([[1, 2], (3, 4, 5)]) ->', flatten([[1, 2], (3, 4, 5)]))
print('flatten([[1], [], [2, 3]]) ->', flatten([[1], [], [2, 3]]))

try:
    print('flatten([[1, 2], "ab"]) ->', flatten([[1, 2], "ab"]))
except TypeError as error:
    print(f'flatten([[1, 2], "ab"]) -> TypeError: {error}')