# MBPP/909
### Completion
def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def previous_palindrome(n):
    """Find the previous palindrome less than the specified number."""
    # Start checking from n-1 downwards
    for num in range(n - 1, -1, -1):
        if is_palindrome(num):
            return num
    return None  # In case there is no palindrome (not expected for positive integers)

# Test case
assert previous_palindrome(99) == 88

# Additional test cases for verification
print(previous_palindrome(100))  # Should return 99
print(previous_palindrome(101))  # Should return 99
print(previous_palindrome(121))  # Should return 111
print(previous_palindrome(200))  # Should return 191
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert previous_palindrome(99)==88
    assert previous_palindrome(1221)==1111
    assert previous_palindrome(120)==111
