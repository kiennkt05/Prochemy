# MBPP/928
### Completion
def change_date_format(date_str):
    """
    Convert a date from 'yyyy-mm-dd' format to 'dd-mm-yyyy' format.

    Parameters:
    date_str (str): The date string in 'yyyy-mm-dd' format.

    Returns:
    str: The date string in 'dd-mm-yyyy' format.
    """
    # Split the input date string into components
    year, month, day = date_str.split('-')
    
    # Rearrange the components to 'dd-mm-yyyy' format
    new_format = f"{day}-{month}-{year}"
    
    return new_format

# Test the function with the provided test case
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
