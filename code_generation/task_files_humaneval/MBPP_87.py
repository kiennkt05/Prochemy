# MBPP/87
### Completion
def merge_dictionaries_three(dict1, dict2, dict3):
    """
    Merges three dictionaries into one. In case of key collisions, 
    the values from the last dictionary will overwrite those from the previous ones.

    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    dict3 (dict): The third dictionary.

    Returns:
    dict: A single dictionary containing all unique keys from the three dictionaries.
    """
    return {**dict1, **dict2, **dict3}

# Test case
assert merge_dictionaries_three(
    {"R": "Red", "B": "Black", "P": "Pink"},
    {"G": "Green", "W": "White"},
    {"O": "Orange", "W": "White", "B": "Black"}
) == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}
