# MBPP/902
### Completion
def add_dict(dict1, dict2):
    combined_dict = {}
    
    # Add values from the first dictionary
    for key, value in dict1.items():
        combined_dict[key] = value
    
    # Add values from the second dictionary
    for key, value in dict2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
            
    return combined_dict

# Test the function with the provided assertion
assert add_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}) == {'a': 400, 'b': 400, 'c': 300, 'd': 400}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 
    assert add_dict({'a': 500, 'b': 700, 'c':900},{'a': 500, 'b': 600, 'd':900})==({'b': 1300, 'd': 900, 'a': 1000, 'c': 900}) 
    assert add_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})
