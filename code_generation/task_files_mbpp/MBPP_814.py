# MBPP/814
### Completion
def rombus_area(d1, d2):
    return (d1 * d2) / 2

# Test the function with the provided assertion
assert rombus_area(10, 20) == 100
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rombus_area(10,20)==100
    assert rombus_area(10,5)==25
    assert rombus_area(4,2)==4
