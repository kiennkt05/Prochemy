# MBPP/92
### Completion
def is_undulating(number: str) -> bool:
    # Check if the input is a valid string of digits
    if not number.isdigit():
        return False
    
    # Check for undulating pattern
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            return False
            
    return True

# Test the function with the provided assertion
assert is_undulating("1212121") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_undulating("1212121") == True
    assert is_undulating("1991") == False
    assert is_undulating("121") == True
