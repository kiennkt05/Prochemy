# MBPP/232
### Completion
import heapq

def larg_nnum(data, n):
    return heapq.nlargest(n, data)

# Test the function with the provided assertion
assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [100, 90]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[100,90]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[100,90,80,70,60]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[100,90,80]
