def trailingZeroes(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# Example usage:
n = 5
print("Number of trailing zeros in", n, "factorial:", trailingZeroes(n))