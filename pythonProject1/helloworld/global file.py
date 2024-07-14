# x=10
# def my_function():
#     global x
#     x=4
#     y=5
#     print(y)
# my_function()
# print(x)

try:
    file = open("example.txt", "r")
    # Perform operations with the file
    print(file.read())
except FileNotFoundError:
    print("Error: File not found!")
finally:
    if 'file' in locals():
        file.close()  # Close the file regardless of exceptions
