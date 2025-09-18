# MBPP/305
### Completion
def start_withp(words):
    # Initialize an empty list to hold words starting with 'p'
    p_words = []
    
    # Iterate through each word in the list
    for word in words:
        # Split the words in the string and check each one
        for w in word.split():
            if w.lower().startswith('p'):
                p_words.append(w)
                # Stop if we have found two words
                if len(p_words) == 2:
                    return tuple(p_words)
    
    # Return None if less than two words are found
    return None

# Test the function with the provided assertion
assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')
