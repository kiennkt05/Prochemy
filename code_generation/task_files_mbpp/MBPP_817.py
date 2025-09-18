# MBPP/817
### Completion
def div_of_nums(numbers, m, n):
    return list(filter(lambda x: x % m == 0 or x % n == 0, numbers))

# Test the function with the provided assertion
assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190], 19, 13) == [19, 65, 57, 39, 152, 190]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],19,13)==[19, 65, 57, 39, 152, 190]
    assert div_of_nums([1, 2, 3, 5, 7, 8, 10],2,5)==[2, 5, 8, 10]
    assert div_of_nums([10,15,14,13,18,12,20],10,5)==[10, 15, 20]
