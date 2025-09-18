# MBPP/64
### Completion
def subject_marks(marks):
    """
    Sorts a list of tuples containing subject names and their corresponding marks.
    
    Args:
    marks (list of tuples): A list where each tuple contains a subject name and its marks.
    
    Returns:
    list of tuples: A sorted list of tuples based on the marks in ascending order.
    """
    # Sort the list of tuples based on the second element (marks) using a lambda function
    sorted_marks = sorted(marks, key=lambda x: x[1])
    return sorted_marks

# Test case
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == \
       [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# If the assertion passes, the function works as expected.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    assert subject_marks([('Telugu',49),('Hindhi',54),('Social',33)])==([('Social',33),('Telugu',49),('Hindhi',54)])
    assert subject_marks([('Physics',96),('Chemistry',97),('Biology',45)])==([('Biology',45),('Physics',96),('Chemistry',97)])
