# MBPP/213
### Completion
def concatenate_strings(tuple1, tuple2):
    """
    Concatenates two tuples of strings element-wise.

    Parameters:
    tuple1 (tuple): The first tuple containing strings.
    tuple2 (tuple): The second tuple containing strings.

    Returns:
    tuple: A new tuple containing the concatenated strings.
    """
    # Ensure both tuples have the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Both tuples must have the same length.")
    
    # Concatenate corresponding elements of the tuples
    concatenated = tuple(f"{s1}{s2}" for s1, s2 in zip(tuple1, tuple2))
    
    return concatenated

# Test case
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
