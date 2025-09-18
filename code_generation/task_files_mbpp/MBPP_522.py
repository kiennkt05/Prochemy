# MBPP/522
### Completion
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    return lis

def longest_decreasing_subsequence(arr):
    n = len(arr)
    lds = [1] * n
    
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    return lds

def lbs(arr):
    if not arr:
        return 0
    
    n = len(arr)
    lis = longest_increasing_subsequence(arr)
    lds = longest_decreasing_subsequence(arr)
    
    max_length = 0
    for i in range(n):
        max_length = max(max_length, lis[i] + lds[i] - 1)
    
    return max_length

# Test the function with the provided assertion
assert lbs([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lbs([0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]) == 7
    assert lbs([1, 11, 2, 10, 4, 5, 2, 1]) == 6
    assert lbs([80, 60, 30, 40, 20, 10]) == 5
