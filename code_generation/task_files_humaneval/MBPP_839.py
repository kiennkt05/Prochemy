# MBPP/839
### Completion
def sort_tuple(tuples_list):
    """
    Sorts a list of tuples alphabetically by the first item of each tuple.

    Parameters:
    tuples_list (list of tuple): A list containing tuples to be sorted.

    Returns:
    list of tuple: A new list of tuples sorted by the first item.
    """
    # Sort the list of tuples using the first item of each tuple as the key
    sorted_list = sorted(tuples_list, key=lambda x: x[0])
    return sorted_list

# Test the function with the provided assertion
assert sort_tuple([("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]) == [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]

# If the assertion passes, the function works correctly.
print("Function works correctly and passed the test case.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_tuple([("Amana", 28), ("Zenat", 30), ("Abhishek", 29),("Nikhil", 21), ("B", "C")]) == [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
    assert sort_tuple([("aaaa", 28), ("aa", 30), ("bab", 29), ("bb", 21), ("csa", "C")]) == [('aa', 30), ('aaaa', 28), ('bab', 29), ('bb', 21), ('csa', 'C')]
    assert sort_tuple([("Sarala", 28), ("Ayesha", 30), ("Suman", 29),("Sai", 21), ("G", "H")]) == [('Ayesha', 30), ('G', 'H'), ('Sai', 21), ('Sarala', 28), ('Suman', 29)]
