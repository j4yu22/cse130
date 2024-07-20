"""
1.
"""


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage
arr = [1, 2, 3, 4, 5]
target = 3
print(binary_search(arr, target))


"""
2.
"""


def get_first_element(arr):
    return arr[0]


# Example usage
arr = [1, 2, 3, 4, 5]
print(get_first_element(arr))


"""
3.
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage
arr = [5, 2, 4, 6, 1, 3]
merge_sort(arr)
print(arr)


"""
4.
"""


def find_max(arr):
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element


# Example usage
arr = [1, 2, 3, 4, 5]
print(find_max(arr))
