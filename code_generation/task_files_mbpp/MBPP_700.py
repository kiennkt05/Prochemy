# MBPP/700
### Completion
def count_range_in_list(lst, lower, upper):
    count = 0
    for num in lst:
        if lower <= num <= upper:
            count += 1
    return count

# Test the function with the provided assertion
assert count_range_in_list([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_range_in_list([10,20,30,40,40,40,70,80,99],40,100)==6
    assert count_range_in_list(['a','b','c','d','e','f'],'a','e')==5
    assert count_range_in_list([7,8,9,15,17,19,45],15,20)==3
