# MBPP/941
### Completion
def count_elim(lst):
    count = 0
    for element in lst:
        if isinstance(element, tuple):
            break
        count += 1
    return count

# Test the function with the provided assertion
assert count_elim([10, 20, 30, (10, 20), 40]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_elim([10,20,30,(10,20),40])==3
    assert count_elim([10,(20,30),(10,20),40])==1
    assert count_elim([(10,(20,30,(10,20),40))])==0
