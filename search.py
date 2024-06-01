# 1. Name:
#      Jay Underwood
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program reads a list of names from a JSON file and uses binary search to determine if a given name is in the list.
# 4. Algorithmic Efficiency:
#      The binary search algorithm has a time complexity of O(log n) because it repeatedly divides the list in half until the target is found or the list is exhausted.
# 5. What was the hardest part? Be as specific as possible:
#      The hardest part of this assignment was figuring out the exact logic for implementing the binary search. It's not something I've actually done before, so it took quite a bit of 'whiteboard' time
#      and trial and error. I'm happy with how it works now though, and I can proudly say I did take the efficiency from O(n) to O(log n), which I'm happy about.
# 6. How long did it take for you to complete the assignment?
#      Total time: 3.25 hours

import json
import os


def read_json_file(filename):
    """
    Reads a JSON file and returns the list of names.
    
    Parameters:
        filename (str): The name of the JSON file to read.
    
    Returns:
        list: The list of names from the JSON file.
    """
    if not os.path.exists(filename):
        print(f"The file {filename} does not exist.")
        return []

    with open(filename, 'r') as file:
        data = json.load(file)
        return data.get('array', [])

def binary_search(sorted_list, target):
    """
    Performs binary search on a sorted list to find the target.
    
    Parameters:
        sorted_list (list): The sorted list to search.
        target (str): The name to search for.
    
    Returns:
        bool: True if the target is found, False otherwise.
    """
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

def main():
    # I added a JSON folder to keep the directory neat.
    folder_path = 'JSON/'
    filename = input("What is the name of the file? ")
    file_path = os.path.join(folder_path, filename)
    
    name_list = read_json_file(file_path)
    
    if not name_list:
        print("This JSON is empty.")
        return
    
    target_name = input("What name are we looking for? ")
    found = binary_search(name_list, target_name)
    
    if found:
        print(f"{target_name} was found in {filename}.")
    else:
        print(f"{target_name} was not found in {filename}.")

if __name__ == "__main__":
    main()
