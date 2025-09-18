# MBPP/326
### Completion
def most_occurrences(strings):
    from collections import Counter
    
    # Join all strings into a single string and split into words
    words = ' '.join(strings).split()
    
    # Count occurrences of each word
    word_count = Counter(words)
    
    # Find the word with the maximum occurrences
    most_common_word, _ = word_count.most_common(1)[0]
    
    return most_common_word

# Test the function with the provided assertion
assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"]) == 'UTS'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
    assert most_occurrences(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
    assert most_occurrences(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'
