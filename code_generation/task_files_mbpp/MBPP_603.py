# MBPP/603
### Completion
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

def find_lucid_numbers(primes, n, current_sum=0, index=0, results=None):
    if results is None:
        results = set()
    
    if current_sum <= n:
        results.add(current_sum)
    
    for i in range(index, len(primes)):
        find_lucid_numbers(primes, n, current_sum + primes[i], i + 1, results)
    
    return results

def get_ludic(n):
    primes = generate_primes(n)
    lucid_numbers = find_lucid_numbers(primes, n)
    return sorted(lucid_numbers)

# Test the function
assert get_ludic(10) == [1, 2, 3, 5, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
