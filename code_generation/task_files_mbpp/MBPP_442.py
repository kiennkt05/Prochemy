# MBPP/442
### Completion
def positive_count(arr):
    if not arr:  # Check for empty array
        return 0.0
    
    positive_numbers = sum(1 for x in arr if x > 0)  # Count positive numbers
    total_numbers = len(arr)  # Total numbers in the array
    
    return positive_numbers / total_numbers  # Calculate the ratio

# Test the function with the provided assertion
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56
