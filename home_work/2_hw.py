def task_1(a, b, c, d, f):
    return a[1], b[2.1], c['строка'], d[1, 2], f[(5 > 4)]


a: int = 1
b: float = 2.1
c: str = 'строка'
d: list = [1, 2]
f: bool = (5 > 4)

print(a, b, c, d, f)

print(a, "относится к типу", type(a))
print(b, "относится к типу", type(b))
print(c, "относится к типу", type(c))
print(d, "относится к типу", type(d))
print(f, "относится к типу", type(f))


def task_2(a=[1, 2, 3, 5, 8, 13, 21]):
    return 'a=[1, 2, 3, 5, 8, 13, 21]'

a=[1, 2, 3, 5, 8, 13, 21]

print('a[0] = ', a[0])
print('a[1] = ', a[1])
print('a[2] = ', a[2])

print([1, 2, 3, 5, 8, 13, 21], "относится к типу", type([1, 2, 3, 5, 8, 13, 21]))


def task_2(a=[1, 2, 3, 5, 8, 13, 21]):
    return 'a=[1, 2, 3, 5, 8, 13, 21]'
print(1, 2, 3, 5, 8, 13, 21, "числа фибоначчи")


def task_3(a):
    return a
a = 5
print(a, "относится к типу", type(a))
print(5 ** 2)