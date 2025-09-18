# MBPP/339
### Completion
def find_Divisor(start, end):
    divisor_count = {}
    
    # Iterate through each number in the interval
    for num in range(start, end + 1):
        # Find divisors of the current number
        for i in range(1, num + 1):
            if num % i == 0:  # i is a divisor of num
                if i in divisor_count:
                    divisor_count[i] += 1
                else:
                    divisor_count[i] = 1
    
    # Find the maximum occurring divisor
    max_divisor = None
    max_count = 0
    
    for divisor, count in divisor_count.items():
        if count > max_count or (count == max_count and divisor > max_divisor):
            max_count = count
            max_divisor = divisor
    
    return max_divisor

# Test the function with the provided assertion
assert find_Divisor(2, 2) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Divisor(2,2) == 2
    assert find_Divisor(2,5) == 2
    assert find_Divisor(5,10) == 2
