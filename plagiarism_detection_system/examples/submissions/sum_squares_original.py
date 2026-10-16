"""An example submission with a running sum of squared even values."""


def even_square_total(values):
    total = 0
    for value in values:
        if value % 2 == 0:
            total += value * value
    return total


if __name__ == "__main__":
    print(even_square_total([1, 2, 3, 4, 5, 6]))
