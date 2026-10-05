def transpose(mat: list[list[float | int]]) -> list[list]:
    """Меняет строки и столбцы местами"""
    if not mat:
        return []
    wd=len(mat[0])
    for row in mat:
        if len(row)!=wd:
            raise ValueError('Строки разной длины')
    res=[]
    for j in range(len(mat[0])):
        new=[]
        for i in range(len(mat)):
            new.append(mat[i][j])
        res.append(new)
    return res


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке"""
    if not mat:
        return []
    wd=len(mat[0])
    for row in mat:
        if len(row)!=wd:
            raise ValueError('Строки разной длины')
    res=[]
    for row in mat:
        n=0
        for x in row:
            n+=x
        res.append(n)
    return res
    

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждому столбцу"""
    if not mat:
            return []
    wd=len(mat[0])
    for row in mat:
        if len(row)!=wd:
            raise ValueError('Строки разной длины')
    res = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        res.append(s)
    return res


#тест-кейсы
print('transpose([[1, 2, 3]]) ->', transpose([[1, 2, 3]]))
print('transpose([[1], [2], [3]]) ->', transpose([[1], [2], [3]]))
print('transpose([[1, 2], [3, 4]]) ->', transpose([[1, 2], [3, 4]]))
print('transpose([]) ->', transpose([]))

try:
    print('transpose([[1, 2], [3]]) ->', transpose([[1, 2], [3]]))
except ValueError as error:
    print(f'transpose([[1, 2], [3]]) -> ValueError: {error}')


print('row_sums([[1, 2, 3], [4, 5, 6]]) ->', row_sums([[1, 2, 3], [4, 5, 6]]))
print('row_sums([[-1, 1], [10, -10]]) ->', row_sums([[-1, 1], [10, -10]]))
print('row_sums([[0, 0], [0, 0]]) ->', row_sums([[0, 0], [0, 0]]))

try:
    print('row_sums([[1, 2], [3]]) ->', row_sums([[1, 2], [3]]))
except ValueError as error:
    print(f'row_sums([[1, 2], [3]]) -> ValueError: {error}')

print('col_sums([[1, 2, 3], [4, 5, 6]]) ->', col_sums([[1, 2, 3], [4, 5, 6]]))
print('col_sums([[-1, 1], [10, -10]]) ->', col_sums([[-1, 1], [10, -10]]))
print('col_sums([[0, 0], [0, 0]]) ->', col_sums([[0, 0], [0, 0]]))

try:
    print('col_sums([[1, 2], [3]]) ->', col_sums([[1, 2], [3]]))
except ValueError as error:
    print(f'col_sums([[1, 2], [3]]) -> ValueError: {error}')