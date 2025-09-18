# MBPP/604
### Completion
def reverse_words(s):
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    return ' '.join(reversed_words)

# Test the function with the provided assertion
assert reverse_words("python program") == "program python"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")
