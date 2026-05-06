def min_operations(n, arr, k):
    remainder = arr[0] % k
    for x in arr:
        if x % k != remainder:
            return -1

    normalized = [x // k for x in arr]
    normalized.sort()
    median = normalized[n // 2]

    operations = 0
    for x in normalized:
        operations += abs(x - median)

    return operations


# Manual test
print(min_operations(5, [2, 4, 6, 8, 10], 2))  # Output: 6
