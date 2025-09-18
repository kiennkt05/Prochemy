# MBPP/21
### Completion
def multiples_of_num(n, m):
    return [n * i for i in range(1, m + 1)]

# Test the function with the provided assertion
assert multiples_of_num(4, 3) == [3, 6, 9, 12]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiples_of_num(4,3)== [3,6,9,12]
    assert multiples_of_num(2,5)== [5,10]
    assert multiples_of_num(9,2)== [2,4,6,8,10,12,14,16,18]
