# MBPP/100
### Completion
def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def next_smallest_palindrome(n):
    """Find the next smallest palindrome greater than the specified number."""
    # Start checking from the next number
    n += 1
    while True:
        if is_palindrome(n):
            return n
        n += 1

# Test case
assert next_smallest_palindrome(99) == 101

# Additional test cases
print(next_smallest_palindrome(100))  # Should return 101
print(next_smallest_palindrome(123))  # Should return 131
print(next_smallest_palindrome(999))  # Should return 1001
print(next_smallest_palindrome(12321))  # Should return 12331
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121
