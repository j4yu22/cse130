# this is my solution, it adds up the sums of what the array is and what it should be, then compares them to see which number isn't there.

def find_missing_number(arr):
    """
    finds the missing number in an array of size n with numbers from 1 to n+1

    params:
        arr (list): the input array containing numbers

    returns:
        int: the missing number
    """
    n = len(arr)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

#quality evaluation

"""
This solution has a time complexity of O(n) because it just needs to go through the array
once to add up the 'actual_sum'. All the other steps are O(1) because they are basic math.
The space complexity is O(1) because this program takes an input of an array, which has a
set size, unlike a list.
"""

# this is what I did to test it, it uses assertions to see if the above function actually does what it should do.

def test_find_missing_number():
    """
    tests the find_missing_number function with various test cases
    
    """
    try:
        assert find_missing_number([1, 2, 3, 5]) == 4
        assert find_missing_number([2, 3, 4, 5]) == 1
        assert find_missing_number([1, 2, 4, 5, 6]) == 3
        assert find_missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10]) == 8
    except AssertionError:
        print("A test case failed")
    else:
        print("All test cases passed")


test_find_missing_number()
