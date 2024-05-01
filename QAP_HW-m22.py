# Функция бинарного поиска
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left

# Функция сортировки списка
def sort_list(arr):
    return sorted(arr)

# Ввод последовательности чисел
sequence = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
number = int(input('Введите любое число: '))

# Сортировка и поиск
sorted_sequence = sort_list(sequence)
position = binary_search(sorted_sequence, number)

# Проверка условия и вывод результата
if position < len(sorted_sequence) and sorted_sequence[position] >= number:
    print(f'''
    Условие: найти номер позиции элемента, который меньше введенного пользователем числа, 
    а следующий за ним больше или равен этому числу.\n
    Позиция элемента, удовлетворяющего условию, равна {position}''')
else:
    print('Такого элемента в последовательности нет.')