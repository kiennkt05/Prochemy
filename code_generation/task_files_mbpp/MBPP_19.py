# MBPP/19
### Completion
def test_duplicate(arr):
    # Use a set to track seen elements
    seen = set()
    for num in arr:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
    return False  # No duplicates found

# Test the function with the provided assertion
assert test_duplicate([1, 2, 3, 4, 5]) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True
