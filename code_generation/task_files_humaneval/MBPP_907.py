# MBPP/907
### Completion
def lucky_num(n):
    # Start with a list of numbers from 1 to a large enough number
    if n < 1:
        return []
    
    # Initialize the list of lucky numbers
    numbers = list(range(1, 2 * n + 1))  # Start with numbers from 1 to 2*n
    index = 1  # Start removing every second number
    
    while index < len(numbers):
        # Remove every (index + 1)th number
        step = numbers[index]
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % step != 0]
        index += 1  # Move to the next index
    
    return numbers[:n]  # Return the first n lucky numbers

# Test the function with the provided assertion
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
