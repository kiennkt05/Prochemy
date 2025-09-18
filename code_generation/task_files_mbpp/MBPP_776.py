# MBPP/776
### Completion
def count_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    
    for i in range(len(s)):
        if (i > 0 and s[i-1] in vowels) or (i < len(s) - 1 and s[i+1] in vowels):
            count += 1
            
    return count

# Test the function with the provided assertion
assert count_vowels('bestinstareels') == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5
