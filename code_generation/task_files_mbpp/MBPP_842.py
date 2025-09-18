# MBPP/842
### Completion
def get_odd_occurence(arr, n):
    # Create a dictionary to count occurrences of each number
    count = {}
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Find and return the number that occurs an odd number of times
    for num, cnt in count.items():
        if cnt % 2 != 0:
            return num

# Test the function with the provided assertion
assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
    assert get_odd_occurence([1, 2, 3, 2, 3, 1, 3], 7) == 3
    assert get_odd_occurence([5, 7, 2, 7, 5, 2, 5], 7) == 5
