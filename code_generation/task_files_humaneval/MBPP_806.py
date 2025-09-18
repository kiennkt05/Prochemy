# MBPP/806
### Completion
def max_run_uppercase(s: str) -> int:
    """
    Function to find the maximum run of uppercase characters in the given string.
    
    Parameters:
    s (str): The input string to be analyzed.
    
    Returns:
    int: The length of the longest run of consecutive uppercase characters.
    """
    max_run = 0  # To keep track of the maximum run found
    current_run = 0  # To count the current run of uppercase characters

    for char in s:
        if char.isupper():  # Check if the character is uppercase
            current_run += 1  # Increment the current run
        else:
            max_run = max(max_run, current_run)  # Update max_run if current_run is greater
            current_run = 0  # Reset current run

    # Final check in case the string ends with uppercase characters
    max_run = max(max_run, current_run)

    return max_run

# Test case
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4
