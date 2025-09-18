# MBPP/213
### Completion
def concatenate_strings(tuple1, tuple2):
    return tuple(f"{s1}{s2}" for s1, s2 in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert concatenate_strings(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_strings(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
    assert concatenate_strings(("Shaik", "Ayesha", "Sanya"), (" Dawood", " Begum", " Singh")) == ('Shaik Dawood', 'Ayesha Begum', 'Sanya Singh')
    assert concatenate_strings(("Harpreet", "Priyanka", "Muskan"), ("Kour", " Agarwal", "Sethi")) == ('HarpreetKour', 'Priyanka Agarwal', 'MuskanSethi')
