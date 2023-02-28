# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# st = 'as 23 fdfdg544'
# print(', '.join(ch for ch in st if ch.isdigit()))
# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# st = 'as 23 fdfdg544 34'
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))


# #################################################################################
#
# list comprehension
#
# 1)є строка:
greeting = 'Hello, world'


# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# print([ch.upper() for ch in greeting])
#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i ** 2 for i in range(50) if i % 2])
#
# function
#
# - створити функцію яка виводить ліст
def show(some_list):
    for i in some_list:
        print(i)


# show([1, 2, 3, 4])
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def maxx(a, b, c):
    res = max(a, b, c)
    print(res)
    return res


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max(*args):
    m = max(args)
    print(m)
    return min(args)


# - створити функцію яка повертає найбільше число з ліста
def max_from_list(numbers):
    return max(numbers)


# - створити функцію яка повертає найменьше число з ліста
def man_from_list(numbers):
    return min(numbers)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def summa(numbers):
    # s = 0
    # for i in numbers:
    #     s += i
    # return s
    return sum(numbers)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg(numbers):
    return sum(numbers) / len(numbers)


#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню
numbers = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def min_num():
    arr = numbers.copy()
    print(min(arr))


def dublicate():
    arr = numbers.copy()
    print(list(set(arr)))


def to_x():
    arr = numbers.copy()
    # print(['X' if not (i + 1) % 4 else item for i, item in enumerate(arr)])
    for i in range(3, len(arr), 4):
        arr[i] = 'X'

    print(arr)

# to_x()


def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


def multi():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            # print(' ' if res // 10 else '  ', end='')
            # print(res, end='')
            print(f'{res:4}', end='')
            j += 1
        print()
        i += 1


def menu():
    while True:
        print('1) знайти мін число')
        print('2) видалити усі дублікати')
        print("3) замінити кожне 4-те значення на 'X'")
        print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
        print('5) вывести табличку множення за допомогою цикла while')
        print('9) Вихід')

        ch = input('make your choose: ')

        if ch == '1':
            min_num()
        elif ch == '2':
            dublicate()
        elif ch == '3':
            to_x()
        elif ch == '4':
            square(10)
        elif ch == '5':
            multi()
        elif ch == '9':
            break


# menu()
ss= [22,4,6,77,8,8]

for i, g in enumerate(ss):
    print(g)
