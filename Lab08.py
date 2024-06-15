# 1. Name:
#      Jay Underwood
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program reads a json, prints all of its values as an unsorted list, and then sorts it using bubble sort into a sorted list alphabetically.
# 4. What was the hardest part? Be as specific as possible:
#      The hardest part of this assignment was implementing the bubble sort algorithm and making sure that it works correctly for all edge cases. I had to do some
#      trouble shooting with actually reading the json file and syntax with that, which I'm sure will come with time as I do more and more python stuff relating to
#      jsons and other files like it.
# 5. How long did it take for you to complete the assignment?
#      Total time: 3 and a half hours

import json
import os
import sys
import traceback

def read_json_file(filename):
    """
    Reads a JSON file and returns the list of names.
    
    Parameters:
        filename (str): The name of the JSON file to read.
    
    Returns:
        list: The list of names from the JSON file.
    """
    assert isinstance(filename, str), "Filename must be a string"

    file_path = os.path.join('JSON', filename)
    
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            names_list = data.get('array', [])
            assert isinstance(names_list, list), "The JSON array must be a list"
            return names_list
    except json.JSONDecodeError:
        print("Error decoding JSON. Ensure the file is correctly formatted.")
        return []

def bubble_sort(arr):
    """
    Sorts a list using the bubble sort algorithm.
    
    Parameters:
        arr (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    try:
        filename = input("What is the name of the file? ")
        name_list = read_json_file(filename)
        
        print(f"Unsorted List: ")
        for name in name_list:
            print(f"\t{name}")
        
        sorted_list = bubble_sort(name_list)
        
        print("\nSorted list:")
        for name in sorted_list:
            print(f"\t{name}")
    
    except Exception as e:
        print("An error occurred:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
