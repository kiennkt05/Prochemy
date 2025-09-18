# MBPP/263
### Completion
def merge_dict(dict1, dict2):
    # Merging dict1 and dict2
    merged_dict = {**dict2, **dict1}
    return merged_dict

# Test the function with the provided assertion
assert merge_dict({'a': 100, 'b': 200}, {'x': 300, 'y': 200}) == {'x': 300, 'y': 200, 'a': 100, 'b': 200}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge_dict({'a': 100, 'b': 200},{'x': 300, 'y': 200})=={'x': 300, 'y': 200, 'a': 100, 'b': 200}
    assert merge_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})=={'a':900,'b':900,'d':900,'a':900,'b':900,'d':900}
    assert merge_dict({'a':10,'b':20},{'x':30,'y':40})=={'x':30,'y':40,'a':10,'b':20}
