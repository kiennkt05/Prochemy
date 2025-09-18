# MBPP/973
### Completion
def left_rotate(s, n):
    # Ensure n is within the bounds of the string length
    n = n % len(s) if s else 0
    return s[n:] + s[:n]

# Test the function with the provided assertion
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
