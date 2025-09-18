# MBPP/806
### Completion
def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    
    for char in s:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
            
    return max_run

# Test the function with the provided assertion
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4
