# MBPP/911
### Completion
import heapq

def maximum_product(arr):
    if len(arr) < 3:
        raise ValueError("Array must contain at least three numbers.")
    
    # Use heapq to find the three largest numbers
    largest_three = heapq.nlargest(3, arr)
    
    # Calculate the product of the three largest numbers
    product = largest_three[0] * largest_three[1] * largest_three[2]
    
    return product

# Test the function with the provided assertion
assert maximum_product([12, 74, 9, 50, 61, 41]) == 225700
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum_product( [12, 74, 9, 50, 61, 41])==225700
    assert maximum_product([25, 35, 22, 85, 14, 65, 75, 25, 58])==414375
    assert maximum_product([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==2520
