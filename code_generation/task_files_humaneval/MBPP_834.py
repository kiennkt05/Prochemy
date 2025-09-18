# MBPP/834
### Completion
def generate_matrix(n):
    # Initialize an n x n matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Define the boundaries of the spiral
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1  # Start filling with number 1
    
    while top <= bottom and left <= right:
        # Fill top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            # Fill bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            # Fill left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
    return matrix

# Test the function with the provided test case
assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert generate_matrix(3)==[[1, 2, 3], [8, 9, 4], [7, 6, 5]] 
    assert generate_matrix(2)==[[1,2],[4,3]]
    assert generate_matrix(7)==[[1, 2, 3, 4, 5, 6, 7], [24, 25, 26, 27, 28, 29, 8], [23, 40, 41, 42, 43, 30, 9], [22, 39, 48, 49, 44, 31, 10], [21, 38, 47, 46, 45, 32, 11], [20, 37, 36, 35, 34, 33, 12], [19, 18, 17, 16, 15, 14, 13]]
