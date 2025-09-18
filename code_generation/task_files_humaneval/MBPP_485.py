# MBPP/485
### Completion
def is_palindrome(num):
    """Check if a number is a palindrome."""
    str_num = str(num)
    return str_num == str_num[::-1]

def largest_palindrome(arr):
    """Find the largest palindromic number in the given array."""
    max_palindrome = -1  # Initialize to -1 to handle cases with no palindromes
    for num in arr:
        if is_palindrome(num):
            max_palindrome = max(max_palindrome, num)
    return max_palindrome if max_palindrome != -1 else None  # Return None if no palindrome found

# Test case
assert largest_palindrome([1, 232, 54545, 999991]) == 54545
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_palindrome([1, 232, 54545, 999991], 4) == 54545
    assert largest_palindrome([1, 2, 3, 4, 5, 50], 6) == 5
    assert largest_palindrome([1, 3, 7, 9, 45], 5)  == 9
