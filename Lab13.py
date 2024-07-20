import json
import os

# 1. Name:
#      Jay Underwood
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program reads power data from a JSON file, prompts the user for the size of the sub-array, and outputs the average value of the sub-array.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was probably the error handling with JSON files. It took me a little research and troubleshooting to get it to work. I got the hang of it after messing with it for a while. The actual logic for the math was pretty straight forward.
# 5. How long did it take for you to complete the assignment?
#      About 4 hours.

def read_file(filename):
    """
    Reads the JSON file and returns the data.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        dict: The data from the JSON file if successful, None otherwise.
    """
    if not os.path.isfile(filename):
        print("The file does not exist.")
        return None
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print("The file is not in JSON format.")
        return None


def validate_data(data):
    """
    Validates if the data has the correct format.

    Parameters:
        data (dict): The data to validate.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    if 'array' not in data or not isinstance(data['array'], list) or not all(isinstance(i, int) for i in data['array']):
        print("The file does not have 'array' as the first key or the value is not an array of integers.")
        return False
    return True


def get_sub_array_size(array_length):
    """
    Prompts the user for the size of the sub-array and validates it.

    Parameters:
        array_length (int): The length of the array.

    Returns:
        int: The size of the sub-array if valid, None otherwise.
    """
    try:
        sub_array_size = int(input("Enter the size of the sub-array: "))
    except ValueError:
        print("The size of the sub-array must be an integer.")
        return None
    if sub_array_size <= 0 or sub_array_size > array_length:
        print("The size of the sub-array is invalid.")
        return None
    return sub_array_size


def calculate_average(sub_array):
    """
    Calculates the average of the sub-array.

    Parameters:
        sub_array (list): The sub-array of integers.

    Returns:
        float: The average of the sub-array.
    """
    assert len(sub_array) > 0, "The sub-array must contain at least one element."
    average_power = sum(sub_array) / len(sub_array)
    return average_power


def main():
    """
    Main
    """
    
    filename = input("Enter the filename: ")
    data = read_file(filename)
    if data is None:
        return

    if not validate_data(data):
        return

    sub_array_size = get_sub_array_size(len(data['array']))
    if sub_array_size is None:
        return

    sub_array = data['array'][:sub_array_size]
    average_power = calculate_average(sub_array)

    print(f"The average power of the sub-array is: {average_power:.2f}")


if __name__ == "__main__":
    main()
