# MBPP/166
### Completion
def find_even_Pair(arr, n):
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Count even and odd numbers in the array
    for number in arr:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Calculate pairs of even numbers
    even_pairs = even_count * (even_count - 1) // 2
    # Calculate pairs of odd numbers
    odd_pairs = odd_count * (odd_count - 1) // 2
    
    # Total pairs with even XOR
    total_even_pairs = even_pairs + odd_pairs
    
    return total_even_pairs

# Test case
assert find_even_Pair([5, 4, 7, 2, 1], 5) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_even_Pair([5,4,7,2,1],5) == 4
    assert find_even_Pair([7,2,8,1,0,5,11],7) == 9
    assert find_even_Pair([1,2,3],3) == 1
