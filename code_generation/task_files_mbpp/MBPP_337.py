# MBPP/337
### Completion
import re

def text_match_word(word, text):
    # Create a regex pattern to match the word at the end of the string with optional punctuation
    pattern = rf"{re.escape(word)}[.!?]?$"
    
    # Use re.search to find the match
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Example usage
assert text_match_word("python", "I love python.") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_word("python.")==('Found a match!')
    assert text_match_word("python.")==('Found a match!')
    assert text_match_word("  lang  .")==('Not matched!')
