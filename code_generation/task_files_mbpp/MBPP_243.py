# MBPP/243
### Completion
def sort_on_occurence(tuples_list):
    from collections import Counter
    
    # Count occurrences of the first elements
    first_elements = [t[0] for t in tuples_list]
    counts = Counter(first_elements)
    
    # Create a sorted list based on the occurrence of the first elements
    sorted_tuples = sorted(tuples_list, key=lambda x: counts[x[0]], reverse=True)
    
    # Prepare the result in the desired format
    result = []
    for key, group in groupby(sorted_tuples, key=lambda x: x[0]):
        result.append((key,) + tuple(item[1] for item in group))
    
    return result

# Test the function with the provided assertion
assert sort_on_occurence([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]) == [(1, 'Jake', 'Cara'), (2, 'Bob')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_on_occurence([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]) == [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]
    assert sort_on_occurence([('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]) == [('b', 'ball', 'b', 2), ('a', 'arm', 'ant', 2)]
    assert sort_on_occurence([(2, 'Mark'), (3, 'Maze'), (2, 'Sara')]) == [(2, 'Mark', 'Sara', 2), (3, 'Maze', 1)]
