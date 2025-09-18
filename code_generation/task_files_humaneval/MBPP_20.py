# MBPP/20
### Completion
def is_woodall(num):
    """
    Check if the given number is a Woodall number.
    
    A Woodall number is defined as n * 2^n - 1 for non-negative integers n.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a Woodall number, False otherwise.
    """
    n = 0
    while True:
        woodall_number = n * (2 ** n) - 1
        if woodall_number == num:
            return True
        elif woodall_number > num:
            return False
        n += 1

# Test case
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
