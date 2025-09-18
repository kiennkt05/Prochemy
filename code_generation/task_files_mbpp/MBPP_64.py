# MBPP/64
### Completion
def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1])

# Test the function with the provided assertion
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    assert subject_marks([('Telugu',49),('Hindhi',54),('Social',33)])==([('Social',33),('Telugu',49),('Hindhi',54)])
    assert subject_marks([('Physics',96),('Chemistry',97),('Biology',45)])==([('Biology',45),('Physics',96),('Chemistry',97)])
