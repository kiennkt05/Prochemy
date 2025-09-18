# MBPP/967
### Completion
def check(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()
    
    # Define the set of all vowels
    vowels = set('aeiou')
    
    # Create a set to track found vowels
    found_vowels = set()
    
    # Iterate through each character in the input string
    for char in input_string:
        # If the character is a vowel, add it to the found_vowels set
        if char in vowels:
            found_vowels.add(char)
    
    # Check if all vowels are found
    if found_vowels == vowels:
        return 'accepted'
    else:
        return 'not accepted'

# Test the function with the provided test case
assert check("SEEquoiaL") == 'accepted'

# Additional test cases
print(check("hello"))  # Should return 'not accepted'
print(check("education"))  # Should return 'accepted'
print(check("AEIOU"))  # Should return 'accepted'
print(check("xyz"))  # Should return 'not accepted'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check("SEEquoiaL") == 'accepted'
    assert check('program') == "not accepted"
    assert check('fine') == "not accepted"
