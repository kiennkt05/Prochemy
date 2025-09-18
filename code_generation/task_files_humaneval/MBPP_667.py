# MBPP/667
### Completion
def Check_Vow(input_string, vowels):
    """
    Count the number of vowels in the input string.

    Parameters:
    input_string (str): The string in which to count vowels.
    vowels (str): A string containing the vowels to check against.

    Returns:
    int: The count of vowels in the input string.
    """
    # Convert both the input string and vowels to lower case for case-insensitive comparison
    input_string = input_string.lower()
    vowels = vowels.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is in the vowels string
        if char in vowels:
            count += 1
            
    return count

# Test case
assert Check_Vow('corner', 'AaEeIiOoUu') == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Vow('corner','AaEeIiOoUu') == 2
    assert Check_Vow('valid','AaEeIiOoUu') == 2
    assert Check_Vow('true','AaEeIiOoUu') ==2
