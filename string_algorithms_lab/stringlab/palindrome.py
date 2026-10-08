"""Manacher's algorithm for the longest palindromic substring."""


def longest_palindrome(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Unique objects avoid a separator collision with user text.
    separator = object()
    sequence: list[object] = [separator]
    for char in text:
        sequence.extend((char, separator))
    radius = [0] * len(sequence)
    center = right = 0
    best_start = best_length = 0
    for i in range(len(sequence)):
        if i < right:
            radius[i] = min(right - i, radius[2 * center - i])
        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < len(sequence) and sequence[i - radius[i] - 1] == sequence[i + radius[i] + 1]:
            radius[i] += 1
        if i + radius[i] > right:
            center, right = i, i + radius[i]
        start = (i - radius[i]) // 2
        if radius[i] > best_length or (radius[i] == best_length and start < best_start):
            best_start, best_length = start, radius[i]
    return text[best_start:best_start + best_length]
