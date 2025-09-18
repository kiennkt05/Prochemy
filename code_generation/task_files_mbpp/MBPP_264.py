# MBPP/264
### Completion
def dog_age(human_years):
    if human_years < 0:
        raise ValueError("Age cannot be negative")
    elif human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4

# Test the function with the provided assertion
assert dog_age(12) == 61
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109
