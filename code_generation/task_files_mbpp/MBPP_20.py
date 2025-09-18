# MBPP/20
### Completion
def is_woodall(num):
    n = 0
    while True:
        woodall_number = n * (2 ** n) - 1
        if woodall_number == num:
            return True
        elif woodall_number > num:
            return False
        n += 1

# Test the function with the provided assertion
assert is_woodall(383) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False
