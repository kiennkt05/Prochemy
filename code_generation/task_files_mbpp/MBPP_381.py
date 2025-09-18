# MBPP/381
### Completion
def index_on_inner_list(data, index):
    return sorted(data, key=lambda x: x[index])

# Test the function with the provided assertion
assert index_on_inner_list([('Greyson Fulton', 98, 99), 
                             ('Brady Kent', 97, 96), 
                             ('Wyatt Knott', 91, 94), 
                             ('Beau Turnbull', 94, 98)], 0) == [
    ('Beau Turnbull', 94, 98), 
    ('Brady Kent', 97, 96), 
    ('Greyson Fulton', 98, 99), 
    ('Wyatt Knott', 91, 94)
]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
    assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,1)==[('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99)]
    assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
