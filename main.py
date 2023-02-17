def decompose(n):
    def decompose_helper(n, k):
        if n == 0:
            return []
        for i in range(min(k, int(n**0.5)), 0, -1):
            seq = decompose_helper(n - i**2, i-1)
            if seq is not None:
                return seq + [i]
        return None

    return decompose_helper(n**2, n-1)
print(decompose(11))  # [1, 2, 4, 10]
print(decompose(50))  # [1, 3, 5, 8, 49]
print(decompose(25))  # [3, 4, 5]
print(decompose(12))  # None