# MBPP/264
### Completion
def dog_age(human_years):
    """
    Calculate a dog's age in dog years based on the human years provided.
    
    The conversion is as follows:
    - The first 2 years of a dog's life count as 10.5 human years each.
    - Each subsequent year counts as 4 human years.
    
    Parameters:
    human_years (int): The age of the dog in human years.
    
    Returns:
    int: The equivalent age of the dog in dog years.
    """
    if human_years <= 2:
        return int(human_years * 10.5)
    else:
        return int(21 + (human_years - 2) * 4)

# Test the function with the provided assertion
assert dog_age(12) == 61

# Additional test cases
assert dog_age(1) == 10  # 1 year in dog years
assert dog_age(2) == 21  # 2 years in dog years
assert dog_age(3) == 25  # 3 years in dog years
assert dog_age(5) == 33  # 5 years in dog years
assert dog_age(10) == 61  # 10 years in dog years

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109
