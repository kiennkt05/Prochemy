# MBPP/265
### Completion
def list_split(input_list, n):
    """
    Splits the input list into sublists for every nth element.

    Parameters:
    input_list (list): The list to be split.
    n (int): The step size for splitting the list.

    Returns:
    list: A list of sublists, each containing elements from the input list.
    """
    # Initialize the result list
    result = []
    
    # Iterate over the range of n to create sublists
    for i in range(n):
        # Create a sublist starting from index i and stepping by n
        sublist = input_list[i::n]
        result.append(sublist)
    
    return result

# Test case
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3) == [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']] 
    assert list_split([1,2,3,4,5,6,7,8,9,10,11,12,13,14],3)==[[1,4,7,10,13], [2,5,8,11,14], [3,6,9,12]] 
    assert list_split(['python','java','C','C++','DBMS','SQL'],2)==[['python', 'C', 'DBMS'], ['java', 'C++', 'SQL']] 
