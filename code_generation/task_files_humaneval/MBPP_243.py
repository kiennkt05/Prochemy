# MBPP/243
### Completion
def sort_on_occurence(tuples_list):
    from collections import defaultdict
    
    # Step 1: Count occurrences of the first elements
    occurrence_count = defaultdict(int)
    for first, _ in tuples_list:
        occurrence_count[first] += 1
    
    # Step 2: Create a dictionary to group second elements by their first element
    grouped_elements = defaultdict(list)
    for first, second in tuples_list:
        grouped_elements[first].append(second)
    
    # Step 3: Sort the first elements based on their occurrence count
    sorted_tuples = sorted(occurrence_count.items(), key=lambda item: item[1], reverse=True)
    
    # Step 4: Prepare the final output format
    result = []
    for first, _ in sorted_tuples:
        result.append((first, *grouped_elements[first]))
    
    return result

# Test case
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
