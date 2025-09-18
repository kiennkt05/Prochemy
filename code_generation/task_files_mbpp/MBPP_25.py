# MBPP/25
### Completion
def find_Product(arr, n):
    # Create a dictionary to count occurrences of each element
    count = {}
    
    # Count occurrences of each element in the array
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Calculate the product of non-repeated elements
    product = 1
    found_non_repeated = False
    for num, cnt in count.items():
        if cnt == 1:  # Check if the element is non-repeated
            product *= num
            found_non_repeated = True
    
    # If no non-repeated elements were found, return 0
    return product if found_non_repeated else 0

# Test the function with the provided assertion
assert find_Product([1, 1, 2, 3], 4) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Product([1,1,2,3],4) == 6
    assert find_Product([1,2,3,1,1],5) == 6
    assert find_Product([1,1,4,5,6],5) == 120
