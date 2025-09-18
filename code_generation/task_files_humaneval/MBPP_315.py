# MBPP/315
### Completion
def find_Max_Len_Even(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize variables to track the maximum even length word
    max_even_word = None
    max_length = 0
    
    # Iterate through each word in the list
    for word in words:
        # Check if the length of the word is even
        if len(word) % 2 == 0:
            # If it's even and longer than the current max, update max_even_word
            if len(word) > max_length:
                max_length = len(word)
                max_even_word = word
    
    return max_even_word

# Test case
assert find_Max_Len_Even("python language") == "language"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Max_Len_Even("python language") == "language"
    assert find_Max_Len_Even("maximum even length") == "length"
    assert find_Max_Len_Even("eve") == "-1"
