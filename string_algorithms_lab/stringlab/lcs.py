"""Longest common subsequence with deterministic reconstruction."""


def longest_common_subsequence(left: str, right: str) -> str:
    if not isinstance(left, str) or not isinstance(right, str):
        raise TypeError("inputs must be strings")
    rows, cols = len(left), len(right)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            dp[i][j] = 1 + dp[i + 1][j + 1] if left[i] == right[j] else max(dp[i + 1][j], dp[i][j + 1])
    result: list[str] = []
    i = j = 0
    while i < rows and j < cols:
        if left[i] == right[j]:
            result.append(left[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return "".join(result)
