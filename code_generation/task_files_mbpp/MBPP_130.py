# MBPP/130
### Completion
def max_occurrences(lst):
    frequency = {}
    
    # Count the frequency of each item in the list
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    # Find the item with the maximum frequency
    max_item = None
    max_count = 0
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            max_item = item
            
    return (max_item, max_count)

# Test the function with the provided assertion
assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == (2, 5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==(2, 5)
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18])==(8, 2)
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==(20, 3)
