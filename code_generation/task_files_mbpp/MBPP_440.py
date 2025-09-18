# MBPP/440
### Completion
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Make sure to download the necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def find_adverb_position(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Get the part-of-speech tags for each word
    tagged_words = pos_tag(words)
    
    # List to hold the positions and adverbs
    adverbs = []
    
    # Iterate through the tagged words
    for index, (word, tag) in enumerate(tagged_words):
        # Check if the tag indicates an adverb
        if tag in ('RB', 'RBR', 'RBS'):
            adverbs.append((index, word))
    
    return adverbs

# Example usage
result = find_adverb_position("clearly!! we can see the sky")
print(result)  # Output should be [(0, 'clearly')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')
