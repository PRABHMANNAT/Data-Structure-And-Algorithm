"""An independently structured search example."""


def locate(sorted_values, target):
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        middle = (low + high) // 2
        current = sorted_values[middle]
        if current == target:
            return middle
        if current < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
