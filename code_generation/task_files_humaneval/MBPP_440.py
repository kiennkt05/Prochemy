# MBPP/440
### Completion
def find_adverb_position(sentence):
    # List of common adverbs (this can be expanded)
    adverbs = [
        'quickly', 'slowly', 'clearly', 'happily', 'sadly', 
        'silently', 'loudly', 'easily', 'hardly', 'very', 
        'too', 'well', 'badly', 'often', 'never', 'always'
    ]
    
    # Normalize the sentence to handle punctuation and case
    words = sentence.split()
    results = []
    
    for word in words:
        # Remove punctuation from the word for accurate matching
        clean_word = ''.join(char for char in word if char.isalnum())
        
        if clean_word in adverbs:
            # Find the starting position of the adverb in the original sentence
            start_index = sentence.find(word)
            end_index = start_index + len(clean_word) - 1
            results.append((start_index, end_index, clean_word))
    
    # Return the first found adverb's position and details, or None if not found
    return results[0] if results else None

# Test case
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')
