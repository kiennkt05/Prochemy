# MBPP/667
### Completion
def Check_Vow(string, vowels):
    # Convert the vowels string to a set for faster lookup
    vowel_set = set(vowels.lower())
    # Count the number of vowels in the string
    count = sum(1 for char in string.lower() if char in vowel_set)
    return count

# Test the function with the provided assertion
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
