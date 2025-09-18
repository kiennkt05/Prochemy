# MBPP/427
### Completion
import re

def change_date_format(date_str):
    # Use regex to match the date format
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        year, month, day = match.groups()
        return f'{day}-{month}-{year}'
    else:
        raise ValueError("Invalid date format. Please use yyyy-mm-dd.")

# Test the function
assert change_date_format("2026-01-02") == '02-01-2026'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'
