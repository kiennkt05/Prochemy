# MBPP/882
### Completion
def parallelogram_perimeter(a, b):
    return 2 * (a + b)

# Assertion to test the function
assert parallelogram_perimeter(10, 20) == 60
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parallelogram_perimeter(10,20)==400
    assert parallelogram_perimeter(15,20)==600
    assert parallelogram_perimeter(8,9)==144
