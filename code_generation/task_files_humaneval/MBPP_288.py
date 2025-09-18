# MBPP/288
### Completion
def modular_inverse(arr, n, p):
    """
    Count the number of elements in the array that have a modular inverse
    equal to themselves under the given prime number p.

    Parameters:
    arr (list): The input array of integers.
    n (int): The number of elements in the array.
    p (int): The prime number under which to calculate the modular inverse.

    Returns:
    int: The count of elements with modular inverse equal to themselves.
    """
    count = 0
    
    for a in arr:
        # Check if a is coprime to p
        if a % p != 0:  # a must not be divisible by p
            # Check if a^2 mod p is equal to 1
            if (a * a) % p == 1:
                count += 1
                
    return count

# Test case
assert modular_inverse([1, 6, 4, 5], 4, 7) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert modular_inverse([ 1, 6, 4, 5 ], 4, 7) == 2
    assert modular_inverse([1, 3, 8, 12, 12], 5, 13) == 3
    assert modular_inverse([2, 3, 4, 5], 4, 6) == 1
