# MBPP/492
### Completion
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Test the function with the provided assertion
assert binary_search([1, 2, 3, 5, 8], 6) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binary_search([1,2,3,5,8], 6) == False
    assert binary_search([7, 8, 9, 10, 13], 10) == True
    assert binary_search([11, 13, 14, 19, 22, 36], 23) == False
