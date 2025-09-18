# MBPP/283
### Completion
def validate(number):
    # Convert the number to a string to iterate over each digit
    str_number = str(number)
    
    # Dictionary to count the frequency of each digit
    frequency = {}
    
    # Count the frequency of each digit
    for digit in str_number:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    
    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, count in frequency.items():
        if count > int(digit):
            return False
    
    return True

# Test case
assert validate(1234) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True
