# MBPP/821
### Completion
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

# Test the function with the provided assertion
assert merge_dictionaries({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}) == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
    assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" },{ "O": "Orange", "W": "White", "B": "Black" })=={'O': 'Orange', 'P': 'Pink', 'B': 'Black', 'W': 'White', 'R': 'Red'}
    assert merge_dictionaries({ "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'W': 'White', 'O': 'Orange', 'G': 'Green', 'B': 'Black'}
