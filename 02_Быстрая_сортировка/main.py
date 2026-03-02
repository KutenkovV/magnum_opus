def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. Опорный элемент — крайний правый
    pivot = arr[-1]

    # 2. Делим на три списка
    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    # 3. Рекурсивно сортируем
    result_1 = quick_sort(less)
    result_2 = equal
    result_3 = quick_sort(greater)

    # 4. Объединяем
    return result_1 + result_2 + result_3

numbers = [5, 8, 9, 4, 2, 9, 1, 8]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)