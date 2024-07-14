def combine_dictionaries(dict1, dict2):
    combined_dict = {}

    # Add keys and values from the first dictionary
    for key, value in dict1.items():
        combined_dict[key] = value

    # Add keys and values from the second dictionary
    for key, value in dict2.items():
        if key in combined_dict:
            # If the key exists in both dictionaries, add their values
            combined_dict[key] += value
        else:
            # If the key is unique, simply add it to the combined dictionary
            combined_dict[key] = value

    return combined_dict

# Example dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 40, 'c': 50, 'd': 60}

# Combine the dictionaries
combined_dictionary = combine_dictionaries(dict1, dict2)

# Print the combined dictionary
print("Combined Dictionary:", combined_dictionary)