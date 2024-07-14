# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


arr = ['X', 'Y', 'X', 'Z', 'Z', 'A', 'Z', 'B', 'Z', 'C', 'C', 'B', 'D']
res = dict()
i = 0

while i < len(arr) - 2:
    suffix = '_' + str(i)
    key = arr[i] + suffix
    res[key] = 0

    while arr[i] == arr[i + 2]:
        res[arr[i] + suffix] += 1
        i += 1
        if i >= len(arr) - 2:
            break
    i += 1

for key, value in res.items():
    element = key.split('_')[0]
    print(f'{element}: {value}')