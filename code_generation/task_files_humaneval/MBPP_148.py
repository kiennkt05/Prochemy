# MBPP/148
### Completion
def sum_digits_twoparts(n):
    # Convert the number to a string to access its digits
    str_n = str(n)
    max_sum = 0
    
    # Iterate through possible split points
    for i in range(1, len(str_n)):  # Split point must be between 1 and len(str_n)-1
        # Split the number into two parts
        part1 = str_n[:i]
        part2 = str_n[i:]
        
        # Calculate the sum of digits for both parts
        sum_part1 = sum(int(digit) for digit in part1)
        sum_part2 = sum(int(digit) for digit in part2)
        
        # Update the maximum sum found
        current_sum = sum_part1 + sum_part2
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function with the provided test case
assert sum_digits_twoparts(35) == 17
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_digits_twoparts(35)==17
    assert sum_digits_twoparts(7)==7
    assert sum_digits_twoparts(100)==19
