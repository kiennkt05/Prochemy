# MBPP/558
### Completion
def digit_distance_nums(num1, num2):
    # Convert both numbers to strings to access each digit
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Pad the shorter number with leading zeros
    max_length = max(len(str_num1), len(str_num2))
    str_num1 = str_num1.zfill(max_length)
    str_num2 = str_num2.zfill(max_length)
    
    # Calculate the digit distance
    distance = sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str_num1, str_num2))
    
    return distance

# Test the function with the provided assertion
assert digit_distance_nums(1, 2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7
