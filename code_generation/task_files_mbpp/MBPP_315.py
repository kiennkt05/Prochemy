# MBPP/315
### Completion
def find_Max_Len_Even(sentence):
    words = sentence.split()
    max_even_word = ""
    
    for word in words:
        if len(word) % 2 == 0:  # Check if the length of the word is even
            if len(word) > len(max_even_word):  # Check if it's longer than the current max
                max_even_word = word
                
    return max_even_word

# Test the function with the provided assertion
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
