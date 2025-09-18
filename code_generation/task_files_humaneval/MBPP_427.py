# MBPP/427
### Completion
import re

def change_date_format(date_str):
    """
    Convert a date from 'yyyy-mm-dd' format to 'dd-mm-yyyy' format using regex.

    Parameters:
    date_str (str): The date string in 'yyyy-mm-dd' format.

    Returns:
    str: The date string in 'dd-mm-yyyy' format.
    """
    # Define the regex pattern to match the date format
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    
    # Use re.sub to rearrange the date format
    new_date = re.sub(pattern, r'\3-\2-\1', date_str)
    
    return new_date

# Test the function with the provided test case
assert change_date_format("2026-01-02") == '02-01-2026'

# You can add more test cases to validate the function
print(change_date_format("2026-01-02"))  # Output: '02-01-2026'
print(change_date_format("1999-12-31"))  # Output: '31-12-1999'
print(change_date_format("2000-02-29"))  # Output: '29-02-2000'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'
