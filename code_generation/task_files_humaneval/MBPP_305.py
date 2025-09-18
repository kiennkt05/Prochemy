# MBPP/305
### Completion
def start_withp(words):
    # Initialize a list to hold words that start with 'p'
    p_words = []
    
    # Iterate through each string in the input list
    for phrase in words:
        # Split the phrase into individual words
        for word in phrase.split():
            # Check if the word starts with 'p' or 'P'
            if word.lower().startswith('p'):
                p_words.append(word)
                
            # If we already have two words, we can return them
            if len(p_words) == 2:
                return (p_words[0], p_words[1])
    
    # If less than two words starting with 'p' were found, return None
    return None

# Test case
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
