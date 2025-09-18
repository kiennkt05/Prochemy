# MBPP/907
### Completion
def lucky_num(n):
    # Start with a list of natural numbers
    numbers = list(range(1, n * 2))  # We need to ensure we have enough numbers
    index = 1  # Start with the second number (index 1)

    while index < len(numbers):
        # Remove every numbers[index]-th number
        step = numbers[index]
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % step != 0]
        index += 1

    return numbers[:n]

# Test the function
assert lucky_num(10) == [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lucky_num(10)==[1, 3, 7, 9, 13, 15, 21, 25, 31, 33] 
    assert lucky_num(5)==[1, 3, 7, 9, 13]
    assert lucky_num(8)==[1, 3, 7, 9, 13, 15, 21, 25]
