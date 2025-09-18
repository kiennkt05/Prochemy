# MBPP/854
### Completion
import heapq

def raw_heap(lst):
    # Convert the list into a heap in-place
    heapq.heapify(lst)
    return lst

# Test the function with the provided assertion
assert raw_heap([25, 44, 68, 21, 39, 23, 89]) == [21, 25, 23, 44, 39, 68, 89]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert raw_heap([25, 44, 68, 21, 39, 23, 89])==[21, 25, 23, 44, 39, 68, 89]
    assert raw_heap([25, 35, 22, 85, 14, 65, 75, 25, 58])== [14, 25, 22, 25, 35, 65, 75, 85, 58]
    assert raw_heap([4, 5, 6, 2])==[2, 4, 6, 5]
