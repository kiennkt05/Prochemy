# MBPP/582
### Completion
def is_empty_dict(d):
    """Check if the given dictionary is empty."""
    return len(d) == 0

# Example usage and assertion
my_dict = {}
assert is_empty_dict(my_dict) == True  # This should be True since my_dict is empty

my_dict = {10: 'value'}
assert is_empty_dict(my_dict) == False  # This should be False since my_dict is not empty
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True
