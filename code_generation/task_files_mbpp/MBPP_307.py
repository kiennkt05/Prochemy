# MBPP/307
### Completion
def colon_tuplex(tup, index, new_value):
    # Convert the tuple to a list
    temp_list = list(tup)
    
    # Replace the element at the specified index with the new value
    temp_list[index] = new_value
    
    # Convert the list back to a tuple
    return tuple(temp_list)

# Test the function with the provided assertion
assert colon_tuplex(("HELLO", 5, [], True), 2, 50) == ("HELLO", 5, [50], True)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)
