def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    a = list(nums)
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:  # обменов не было - уже отсортировано
            break
    return a


def insertion_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    a = list(nums)
    for i in range(1, len(a)):
        cur = a[i]
        j = i - 1
        while j >= 0 and a[j] > cur:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a


def selection_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    a = list(nums)
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a