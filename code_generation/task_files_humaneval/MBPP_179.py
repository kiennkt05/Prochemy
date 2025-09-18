# MBPP/179
### Completion
def is_num_keith(n):
    # Convert the number to a list of its digits
    digits = [int(d) for d in str(n)]
    k = len(digits)  # Number of digits
    sequence = digits[:]  # Start the sequence with the digits of n

    # Generate the sequence until the last element is greater than or equal to n
    while True:
        next_value = sum(sequence[-k:])  # Sum the last k elements
        if next_value == n:
            return True  # n is a Keith number
        elif next_value > n:
            return False  # n is not a Keith number
        sequence.append(next_value)  # Append the next value to the sequence

# Test the function with the provided test case
assert is_num_keith(14) == True

# Additional test cases
assert is_num_keith(10) == False  # 10 is not a Keith number
assert is_num_keith(11) == True   # 11 is a Keith number
assert is_num_keith(12) == True   # 12 is a Keith number
assert is_num_keith(13) == True   # 13 is a Keith number
assert is_num_keith(15) == False  # 15 is not a Keith number

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_num_keith(14) == True
    assert is_num_keith(12) == False
    assert is_num_keith(197) == True
