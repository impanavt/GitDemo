# Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
#    Array: positive integers. We have to find the maximum difference between j-i where array[j] > array[i]
# Solution:
# Calculate the length of the array and initiate max difference with -1.
# Run two loops. The outer loop picks elements from the left, and the inner loop compares the picked elements with elements starting from the right side.
# Stop the inner loop when the element is greater than the picked element and keep updating the maximum difference using j - I.
# Examples:
# Input: [20, 70, 40, 50, 12, 38, 98], Output: 6  (j = 6, i = 0)
# Input: [10, 3, 2, 4, 5, 6, 7, 8, 18, 0], Output: 8 ( j = 8, i = 0)

# def max_index_diff(array):
#     n = len(array)
#     max_diff = -1
#     for i in range(0, n):
#         j = n - 1
#         while (j > i):
#             if array[j] > array[i] and max_diff < (j - i):
#                 max_diff = j - i
#             j -= 1
#
#     return max_diff
#
#
# array_1 = [20, 70, 40, 50, 12, 38, 98]
#
# res=max_index_diff(array_1)
# print(res)


def max_index_diff(arr):
    n = len(arr)
    max_diff = -1

    # Run two loops to compare elements
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] > arr[i] and max_diff < (j - i):
                max_diff = j - i

    return max_diff

# Example usage:
arr1 = [20, 70, 40, 50, 12, 38, 98]
arr2 = [10, 3, 2, 4, 5, 6, 7, 8, 18, 0]

print("Maximum difference for arr1:", max_index_diff(arr1))  # Output: 6
print("Maximum difference for arr2:", max_index_diff(arr2))  # Output