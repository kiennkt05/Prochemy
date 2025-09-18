# MBPP/781
### Completion
def count_Divisors(n):
    if n <= 0:
        return "Invalid input"
    
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            
    return "Even" if count % 2 == 0 else "Odd"

# Test the function with the provided assertion
assert count_Divisors(10) == "Even"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Divisors(10) == "Even"
    assert count_Divisors(100) == "Odd"
    assert count_Divisors(125) == "Even"
