# MBPP/928
### Completion
def change_date_format(date_str):
    # Split the input date string by '-'
    year, month, day = date_str.split('-')
    # Rearrange the components to the desired format
    return f"{day}-{month}-{year}"

# Test the function with the provided assertion
assert change_date_format('2026-01-02') == '02-01-2026'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert change_date_format('2026-01-02')=='02-01-2026'
    assert change_date_format('2021-01-04')=='04-01-2021'
    assert change_date_format('2030-06-06')=='06-06-2030'
