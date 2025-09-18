# MBPP/745
### Completion
def divisible_by_digits(start, end):
    """
    Find all numbers in the range [start, end] where each number is divisible by every digit it contains.
    
    Parameters:
    start (int): The starting number of the range (inclusive).
    end (int): The ending number of the range (inclusive).
    
    Returns:
    List[int]: A list of numbers that are divisible by all their non-zero digits.
    """
    valid_numbers = []
    
    for number in range(start, end + 1):
        str_number = str(number)
        is_valid = True
        
        for digit in str_number:
            digit_int = int(digit)
            # Check if the digit is zero or if the number is not divisible by the digit
            if digit_int == 0 or number % digit_int != 0:
                is_valid = False
                break
        
        if is_valid:
            valid_numbers.append(number)
    
    return valid_numbers

# Test the function with the provided test case
assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20,25)==[22, 24]
