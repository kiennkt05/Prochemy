# MBPP/828
### Completion
def count_alpha_dig_spl(input_string):
    """
    Count the number of alphabets, digits, and special characters in the input string.

    Parameters:
    input_string (str): The string to be analyzed.

    Returns:
    tuple: A tuple containing three integers:
           (number of alphabets, number of digits, number of special characters)
    """
    alpha_count = 0
    digit_count = 0
    special_count = 0

    for char in input_string:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return (alpha_count, digit_count, special_count)

# Test case
assert count_alpha_dig_spl("abc!@#123") == (3, 3, 3)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_alpha_dig_spl("abc!@#123")==(3,3,3)
    assert count_alpha_dig_spl("dgsuy@#$%&1255")==(5,4,5)
    assert count_alpha_dig_spl("fjdsif627348#%$^&")==(6,6,5)
