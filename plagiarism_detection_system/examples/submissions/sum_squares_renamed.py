"""A deliberately renamed version for the sample similarity report."""


def calculate(numbers):
    answer = 0
    for item in numbers:
        if item % 2 == 0:
            answer += item * item
    return answer


if __name__ == "__main__":
    print(calculate([9, 8, 7, 6, 5, 4]))
