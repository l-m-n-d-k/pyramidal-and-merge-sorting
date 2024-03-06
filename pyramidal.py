# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Инициализируйте наибольший размер как корень
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    lenth = len(arr)

    # Построение max-heap.
    for i in range(lenth, -1, -1):
        heapify(arr, lenth, i)

    # Один за другим извлекаем элементы
    for i in range(lenth-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)

# Управляющий код для тестирования
arr = [5, 16, 8, 14, 20, 1, 26]
print(f'Начальный список: {arr}')
heapSort(arr)
print(f'Отсортированный список: {arr}')