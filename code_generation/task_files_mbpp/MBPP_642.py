# MBPP/642
### Completion
def remove_similar_row(matrix):
    # Use a set to store unique rows
    unique_rows = set()
    
    # Iterate through each row in the matrix
    for row in matrix:
        # Add the row to the set (sets automatically handle duplicates)
        unique_rows.add(tuple(row))
    
    return unique_rows

# Test the function with the provided assertion
assert remove_similar_row([[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]]) == {((2, 2), (4, 6)), ((3, 2), (4, 5))}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_similar_row([[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]] ) == {((2, 2), (4, 6)), ((3, 2), (4, 5))}
    assert remove_similar_row([[(5, 6), (4, 3)], [(3, 3), (5, 7)], [(4, 3), (5, 6)]] ) == {((4, 3), (5, 6)), ((3, 3), (5, 7))}
    assert remove_similar_row([[(6, 7), (5, 4)], [(4, 4), (6, 8)], [(5, 4), (6, 7)]] ) =={((4, 4), (6, 8)), ((5, 4), (6, 7))}
