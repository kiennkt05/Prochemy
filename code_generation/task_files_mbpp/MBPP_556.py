# MBPP/556
### Completion
def find_Odd_Pair(arr, n):
    even_count = 0
    odd_count = 0
    
    # Count even and odd numbers
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    # The number of pairs with odd XOR is the product of even and odd counts
    return even_count * odd_count

# Test the function with the provided assertion
assert find_Odd_Pair([5, 4, 7, 2, 1], 5) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
    assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
    assert find_Odd_Pair([1,2,3],3) == 2
