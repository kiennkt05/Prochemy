# MBPP/904
### Completion
def even_num(n):
    # Check if the number is an integer and if it is even
    if isinstance(n, int):
        return n % 2 == 0
    return False

# Test the function with the provided assertion
assert even_num(13.5) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_num(13.5)==False
    assert even_num(0)==True
    assert even_num(-9)==False
