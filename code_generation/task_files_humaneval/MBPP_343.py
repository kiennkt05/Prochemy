# MBPP/343
### Completion
def dig_let(s):
    """
    Calculate the number of letters and digits in a given string.

    Parameters:
    s (str): The input string to analyze.

    Returns:
    tuple: A tuple containing two integers:
           - The first integer is the count of letters.
           - The second integer is the count of digits.
    """
    letter_count = 0
    digit_count = 0
    
    for char in s:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
            
    return (letter_count, digit_count)

# Test case
assert dig_let("python") == (6, 0)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dig_let("python")==(6,0)
    assert dig_let("program")==(7,0)
    assert dig_let("python3.0")==(6,2)
