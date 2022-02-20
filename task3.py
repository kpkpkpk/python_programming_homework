numbers = list(map(int, input().split(',')))


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array


def gnome_sort(array):
    i = 1
    while i < len(array):
        if array[i - 1] <= array[i]:
            i += 1
        else:
            tmp = array[i]
            array[i] = array[i - 1]
            array[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return array


# https://coderslegacy.com/python/bucket-sort-algorithm/
def bucket_sort(array):
    largest = max(array)
    length = len(array)
    size = largest / length
    buckets = [[] for _ in range(length)]
    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result


# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[].
# n - размер кучи
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if left < n and arr[i] < arr[left]:
        largest = left
    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if right < n and arr[largest] < arr[right]:
        largest = right
    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Применяем heapify к корню.
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Построение max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# heap_sort(numbers)
# print(numbers)
# print(bubble_sort(numbers))
# print(bucket_sort(numbers))
# print(gnome_sort(numbers))
