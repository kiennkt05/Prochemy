# MBPP/10
### Completion
import heapq

def small_nnum(data, n):
    """Return the n smallest items from the dataset."""
    return heapq.nsmallest(n, data)

# Test the function with the provided assertion
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [10, 20]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20]
    assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[10,20,20,40,50]
    assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[10,20,20]
