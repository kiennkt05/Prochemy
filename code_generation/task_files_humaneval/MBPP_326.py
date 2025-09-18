# MBPP/326
### Completion
def most_occurrences(strings):
    # Step 1: Combine all strings into a single string
    combined_string = ' '.join(strings)
    
    # Step 2: Split the combined string into words
    words = combined_string.split()
    
    # Step 3: Count occurrences of each word
    word_count = {}
    for word in words:
        # Normalize the word to lower case to ensure case insensitivity
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Step 4: Find the word with the maximum occurrences
    most_frequent_word = None
    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
    
    return most_frequent_word

# Test case
assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"]) == 'uts'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
    assert most_occurrences(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
    assert most_occurrences(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'
