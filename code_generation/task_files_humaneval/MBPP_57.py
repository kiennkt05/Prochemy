# MBPP/57
### Completion
def find_Max_Num(digits, n):
    """
    Function to find the largest number that can be formed with the given digits.
    
    Parameters:
    digits (list): A list of integers representing the digits.
    n (int): The number of digits to consider (not used in this implementation).
    
    Returns:
    int: The largest number that can be formed from the digits.
    """
    # Convert digits to strings for sorting
    str_digits = [str(digit) for digit in digits]
    
    # Sort the digits in descending order
    str_digits.sort(reverse=True)
    
    # Join the sorted digits to form the largest number
    largest_number = ''.join(str_digits)
    
    # Convert the result back to an integer
    return int(largest_number)

# Test case
assert find_Max_Num([1, 2, 3], 3) == 321
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Max_Num([1,2,3],3) == 321
    assert find_Max_Num([4,5,6,1],4) == 6541
    assert find_Max_Num([1,2,3,9],4) == 9321
