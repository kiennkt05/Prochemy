# MBPP/107
### Completion
def count_Hexadecimal(start, end):
    """
    Count the number of hexadecimal numbers in the given range [start, end].
    
    Parameters:
    start (int): The starting integer of the range.
    end (int): The ending integer of the range.
    
    Returns:
    int: The count of hexadecimal numbers in the range.
    """
    # Initialize the count of hexadecimal numbers
    count = 0
    
    # Iterate through the range from start to end (inclusive)
    for num in range(start, end + 1):
        # Every integer in this range is a valid hexadecimal number
        count += 1
    
    return count

# Test case
assert count_Hexadecimal(10, 15) == 6  # There are 6 numbers: 10, 11, 12, 13, 14, 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Hexadecimal(10,15) == 6
    assert count_Hexadecimal(2,4) == 0
    assert count_Hexadecimal(15,16) == 1
