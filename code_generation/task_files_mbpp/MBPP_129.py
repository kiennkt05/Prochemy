# MBPP/129
### Completion
def magic_square_test(square):
    n = len(square)
    
    # Calculate the magic constant
    magic_constant = n * (n**2 + 1) // 2
    
    # Check the sum of each row
    for row in square:
        if sum(row) != magic_constant:
            return False
    
    # Check the sum of each column
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != magic_constant:
            return False
    
    # Check the sum of the main diagonal
    if sum(square[i][i] for i in range(n)) != magic_constant:
        return False
    
    # Check the sum of the secondary diagonal
    if sum(square[i][n - 1 - i] for i in range(n)) != magic_constant:
        return False
    
    return True

# Test the function with the provided assertion
assert magic_square_test([[7, 12, 1, 14], 
                           [2, 13, 8, 11], 
                           [16, 3, 10, 5], 
                           [9, 6, 15, 4]]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False
