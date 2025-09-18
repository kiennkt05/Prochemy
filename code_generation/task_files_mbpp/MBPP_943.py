# MBPP/943
### Completion
import heapq

def combine_lists(list1, list2):
    return list(heapq.merge(list1, list2))

# Test the function with the provided assertion
assert combine_lists([1, 3, 5, 7, 9, 11], [0, 2, 4, 6, 8, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert combine_lists([1, 3, 5, 7, 9, 11],[0, 2, 4, 6, 8, 10])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert combine_lists([1, 3, 5, 6, 8, 9], [2, 5, 7, 11])==[1,2,3,5,5,6,7,8,9,11]
    assert combine_lists([1,3,7],[2,4,6])==[1,2,3,4,6,7]
