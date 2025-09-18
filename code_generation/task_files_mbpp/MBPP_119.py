# MBPP/119
### Completion
def search(arr, n):
    left, right = 0, n - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Check if mid is even or odd
        if mid % 2 == 0:
            # If mid is even, the single element must be on the right side if arr[mid] == arr[mid + 1]
            if arr[mid] == arr[mid + 1]:
                left = mid + 2
            else:
                right = mid
        else:
            # If mid is odd, the single element must be on the right side if arr[mid] == arr[mid - 1]
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid
    
    # When left == right, we found the single element
    return arr[left]

# Test the function
assert search([1, 1, 2, 2, 3], 5) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert search([1,1,2,2,3],5) == 3
    assert search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
    assert search([1,2,2,3,3,4,4],7) == 1
