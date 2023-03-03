from typing import NoReturn


def square(n: int) -> NoReturn:
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


square(5)


# const myFunc = (a,b)=>a+b;

# myFunc = lambda a, b: a + b


def func():
    a = 0

    def set_a(new_var):
        nonlocal a
        a = new_var

    def get_a():
        nonlocal a
        print(a)

    def resset():
        nonlocal a
        a = 0

    return set_a, get_a, resset


set_a, get_a, resset = func()
get_a()
set_a(555)
get_a()
resset()
get_a()
