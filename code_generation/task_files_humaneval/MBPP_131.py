# MBPP/131
### Completion
def reverse_vowels(s: str) -> str:
    # Define a set of vowels for easy lookup
    vowels = set('aeiouAEIOU')
    
    # Convert the string to a list to allow modification
    s_list = list(s)
    
    # Find all the vowels in the string
    vowel_positions = [i for i, char in enumerate(s_list) if char in vowels]
    vowel_values = [s_list[i] for i in vowel_positions]
    
    # Reverse the list of vowel values
    vowel_values.reverse()
    
    # Replace the vowels in the original list with the reversed vowels
    for pos, value in zip(vowel_positions, vowel_values):
        s_list[pos] = value
    
    # Join the list back into a string and return
    return ''.join(s_list)

# Test case
assert reverse_vowels("Python") == "Python"

# Additional test cases
assert reverse_vowels("hello") == "holle"
assert reverse_vowels("leetcode") == "leotcede"
assert reverse_vowels("aA") == "Aa"
assert reverse_vowels("racecar") == "racecar"
assert reverse_vowels(" ") == " "

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"
