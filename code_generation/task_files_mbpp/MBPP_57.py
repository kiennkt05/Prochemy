# MBPP/57
### Completion
def find_Max_Num(digits, n):
    # Convert the list of digits to strings
    digits_str = list(map(str, digits))
    
    # Sort the digits in descending order
    digits_str.sort(reverse=True)
    
    # Join the sorted digits to form the largest number
    largest_num = int(''.join(digits_str))
    
    return largest_num

# Test the function with the provided assertion
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
