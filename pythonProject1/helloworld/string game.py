
def calculate_lcm(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result
numbers = [12, 18]
lcm_result = calculate_lcm(numbers)
print("LCM of", numbers, "is:", lcm_result)  # Output: LCM of [12, 18, 24] is: 72