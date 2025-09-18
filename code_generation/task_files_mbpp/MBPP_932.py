# MBPP/932
### Completion
def remove_duplic_list(words):
    # Use a set to track seen words and maintain order
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result

# Test the function with the provided assertion
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
