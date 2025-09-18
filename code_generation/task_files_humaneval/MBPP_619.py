# MBPP/619
### Completion
def move_num(s: str) -> str:
    # Initialize empty strings for letters and numbers
    letters = ''
    numbers = ''
    
    # Iterate through each character in the input string
    for char in s:
        if char.isdigit():
            # If the character is a digit, add it to the numbers string
            numbers += char
        else:
            # If the character is a letter, add it to the letters string
            letters += char
            
    # Concatenate letters and numbers and return the result
    return letters + numbers

# Test case
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
