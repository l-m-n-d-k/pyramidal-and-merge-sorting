def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину списка
        left_half = arr[:mid]  # Делаем срез для левой половины
        right_half = arr[mid:]  # Делаем срез для правой половины

        # Рекурсивно сортируем обе половины
        merge_sort(left_half)
        merge_sort(right_half)

        # Индексы для итерации по двум половинам и основному списку
        i = j = k = 0

        # Слияние двух половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Копирование оставшихся элементов левой половины, если они есть
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Копирование оставшихся элементов правой половины, если они есть
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
print("Исходный массив:", arr)
merge_sort(arr)
print("Отсортированный массив:", arr)