# MBPP/22
### Completion
def find_first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None  # Return None if no duplicate is found

# Test the function with the provided assertion
assert find_first_duplicate([1, 2, 3, 4, 4, 5]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_first_duplicate(([1, 2, 3, 4, 4, 5]))==4
    assert find_first_duplicate([1, 2, 3, 4])==-1
    assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2])==1
