# MBPP/619
### Completion
def move_num(s):
    letters = ''.join(filter(str.isalpha, s))
    numbers = ''.join(filter(str.isdigit, s))
    return letters + numbers

# Test the function with the provided assertion
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
