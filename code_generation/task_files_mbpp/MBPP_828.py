# MBPP/828
### Completion
def count_alpha_dig_spl(input_string):
    alphabets = 0
    digits = 0
    special_chars = 0
    
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1
            
    return (alphabets, digits, special_chars)

# Test the function with the provided assertion
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
