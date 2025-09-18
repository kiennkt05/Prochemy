# MBPP/973
### Completion
def left_rotate(s: str, n: int) -> str:
    """
    Left rotates the string `s` by `n` positions.

    Parameters:
    s (str): The string to be rotated.
    n (int): The number of positions to rotate the string.

    Returns:
    str: The left rotated string.
    """
    if not s:  # Check if the string is empty
        return s
    
    n = n % len(s)  # Handle cases where n is greater than the length of the string
    return s[n:] + s[:n]  # Perform the left rotation using slicing

# Test case
assert left_rotate("python", 2) == "thonpy"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert left_rotate("python",2) == "thonpy"   
    assert left_rotate("bigdata",3 ) == "databig" 
    assert left_rotate("hadoop",1 ) == "adooph" 
