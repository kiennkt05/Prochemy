# MBPP/370
### Completion
def float_sort(tuples):
    return sorted(tuples, key=lambda x: float(x[1]), reverse=True)

# Test the function with the provided assertion
assert float_sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]) == [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert float_sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])==[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 
    assert float_sort([('item1', '15'), ('item2', '10'), ('item3', '20')])==[('item3', '20'), ('item1', '15'), ('item2', '10')] 
    assert float_sort([('item1', '5'), ('item2', '10'), ('item3', '14')])==[('item3', '14'), ('item2', '10'), ('item1', '5')] 
