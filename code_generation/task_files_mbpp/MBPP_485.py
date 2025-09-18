# MBPP/485
### Completion
def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def largest_palindrome(arr, n):
    """Find the largest palindromic number in the given array."""
    palindromes = [num for num in arr if is_palindrome(num)]
    return max(palindromes) if palindromes else None

# Test the function with the provided assertion
assert largest_palindrome([1, 232, 54545, 999991], 4) == 54545
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_palindrome([1, 232, 54545, 999991], 4) == 54545
    assert largest_palindrome([1, 2, 3, 4, 5, 50], 6) == 5
    assert largest_palindrome([1, 3, 7, 9, 45], 5)  == 9
