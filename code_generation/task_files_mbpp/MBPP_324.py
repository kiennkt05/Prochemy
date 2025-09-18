# MBPP/324
### Completion
def sum_of_alternates(numbers):
    even_sum = sum(numbers[i] for i in range(0, len(numbers), 2))
    odd_sum = sum(numbers[i] for i in range(1, len(numbers), 2))
    return (even_sum, odd_sum)

# Test the function with the provided assertion
assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_of_alternates((5, 6, 3, 6, 10, 34)) == (46, 18)
    assert sum_of_alternates((1, 2, 3, 4, 5)) == (6, 9)
    assert sum_of_alternates((6, 7, 8, 9, 4, 5)) == (21, 18)
