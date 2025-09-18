# MBPP/648
### Completion
def exchange_elements(lst):
    # Iterate through the list in steps of 2
    for i in range(0, len(lst) - 1, 2):
        # Swap the elements at index i and i+1
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

# Test the function with the provided assertion
assert exchange_elements([0, 1, 2, 3, 4, 5]) == [1, 0, 3, 2, 5, 4]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert exchange_elements([0,1,2,3,4,5])==[1, 0, 3, 2, 5, 4] 
    assert exchange_elements([5,6,7,8,9,10])==[6,5,8,7,10,9] 
    assert exchange_elements([25,35,45,55,75,95])==[35,25,55,45,95,75] 
