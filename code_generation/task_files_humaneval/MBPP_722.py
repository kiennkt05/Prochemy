# MBPP/722
### Completion
def filter_data(students, min_height, min_width):
    """
    Filters students based on minimum height and width.

    Parameters:
    students (dict): A dictionary where keys are student names and values are tuples of (height, width).
    min_height (float): The minimum height to filter students.
    min_width (float): The minimum width to filter students.

    Returns:
    dict: A dictionary of students who meet or exceed the minimum height and width.
    """
    filtered_students = {}
    
    for name, (height, width) in students.items():
        if height >= min_height and width >= min_width:
            filtered_students[name] = (height, width)
    
    return filtered_students

# Test case
assert filter_data({'Cierra Vega': (6.2, 70), 
                    'Alden Cantrell': (5.9, 65), 
                    'Kierra Gentry': (6.0, 68), 
                    'Pierre Cox': (5.8, 66)}, 6.0, 70) == {'Cierra Vega': (6.2, 70)}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.9,67)=={'Cierra Vega': (6.2, 70),'Kierra Gentry': (6.0, 68)}
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.7,64)=={'Cierra Vega': (6.2, 70),'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}
