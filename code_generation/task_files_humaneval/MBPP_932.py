# MBPP/932
### Completion
def remove_duplic_list(words):
    """
    Remove duplicate words from a given list of strings while maintaining the order of first appearances.

    Parameters:
    words (list): A list of strings from which duplicates need to be removed.

    Returns:
    list: A list containing unique strings in the order of their first appearance.
    """
    seen = set()  # To track seen words
    unique_words = []  # To store the result with unique words

    for word in words:
        if word not in seen:
            seen.add(word)  # Mark the word as seen
            unique_words.append(word)  # Add to the result list

    return unique_words

# Test case
assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises"]) == ['Python', 'Exercises', 'Practice', 'Solution']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises"])==['Python', 'Exercises', 'Practice', 'Solution']
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","Java"])==['Python', 'Exercises', 'Practice', 'Solution', 'Java']
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","C++","C","C++"])==['Python', 'Exercises', 'Practice', 'Solution','C++','C']
