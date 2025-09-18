# MBPP/909
### Completion
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def previous_palindrome(n):
    # Start checking from the number just below n
    n -= 1
    while n >= 0:
        if is_palindrome(n):
            return n
        n -= 1
    return None  # In case there is no previous palindrome (for n = 0)

# Test the function with the provided assertion
assert previous_palindrome(99) == 88
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert previous_palindrome(99)==88
    assert previous_palindrome(1221)==1111
    assert previous_palindrome(120)==111
