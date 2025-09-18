# MBPP/844
### Completion
def get_Number(k, n):
    """
    Function to find the k-th element in an array containing the first n odd elements
    followed by the first n even elements.
    
    Parameters:
    k (int): The 1-based index of the element to retrieve.
    n (int): The number of odd and even elements to include in the array.
    
    Returns:
    int: The k-th element in the constructed array.
    """
    # Calculate the k-th element based on the index
    if k <= n:  # If k is within the range of odd numbers
        return 2 * k - 1  # k-th odd number
    else:  # If k is within the range of even numbers
        return 2 * (k - n)  # (k-n)-th even number

# Test case
assert get_Number(8, 5) == 2  # The 8th element is the 3rd even number, which is 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Number(8,5) == 2
    assert get_Number(7,2) == 3
    assert get_Number(5,2) == 3
