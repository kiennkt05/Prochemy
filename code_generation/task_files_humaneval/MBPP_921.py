# MBPP/921
### Completion
def chunk_tuples(input_tuple, n):
    """
    Splits the input tuple into chunks of size n.

    Parameters:
    input_tuple (tuple): The tuple to be chunked.
    n (int): The size of each chunk.

    Returns:
    list: A list of tuples, each of size n.
    """
    # Initialize an empty list to hold the chunks
    chunks = []
    
    # Iterate over the input tuple in steps of n
    for i in range(0, len(input_tuple), n):
        # Create a chunk of size n and append it to the list
        chunk = input_tuple[i:i + n]
        chunks.append(chunk)
    
    return chunks

# Test the function with the provided test case
assert chunk_tuples((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert chunk_tuples((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
    assert chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 2) == [(1, 2), (3, 4), (5, 6), (7, 8), (9,)]
    assert chunk_tuples((11, 14, 16, 17, 19, 21, 22, 25), 4) == [(11, 14, 16, 17), (19, 21, 22, 25)]
