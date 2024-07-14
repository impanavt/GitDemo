def print_full_name(first_name, last_name):
    greeting = "Hello"
    message = "You just delved into python"
    full_name = f"{greeting} {first_name} {last_name}! {message}"
    return full_name

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    result = print_full_name(first_name, last_name)
    # print_full_name is called with first_name and last_name as arguments
    print(result)