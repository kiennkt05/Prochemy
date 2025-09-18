# MBPP/629
### Completion
def Split(mixed_list):
    """
    Function to find even numbers from a mixed list.
    
    Parameters:
    mixed_list (list): A list of integers.
    
    Returns:
    list: A list containing only the even numbers from the input list.
    """
    # Initialize an empty list to store even numbers
    even_numbers = []
    
    # Iterate through each number in the input list
    for number in mixed_list:
        # Check if the number is even
        if number % 2 == 0:
            # Append the even number to the list
            even_numbers.append(number)
    
    # Return the list of even numbers
    return even_numbers

# Test case
assert Split([1, 2, 3, 4, 5]) == [2, 4]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Split([1,2,3,4,5]) == [2,4]
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
    assert Split ([8,12,15,19]) == [8,12]
