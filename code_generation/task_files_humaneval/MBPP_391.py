# MBPP/391
### Completion
def convert_list_dictionary(ids, names, scores):
    """
    Convert three lists (ids, names, scores) into a list of nested dictionaries.
    
    Args:
    ids (list): A list of IDs.
    names (list): A list of names corresponding to the IDs.
    scores (list): A list of scores corresponding to the IDs.
    
    Returns:
    list: A list of nested dictionaries where each dictionary contains an ID as the key
          and another dictionary with the name and score as the value.
    """
    # Check if all lists are of the same length
    if not (len(ids) == len(names) == len(scores)):
        raise ValueError("All input lists must have the same length.")
    
    result = []
    
    # Iterate through the lists and create the nested dictionary
    for i in range(len(ids)):
        nested_dict = {ids[i]: {names[i]: scores[i]}}
        result.append(nested_dict)
    
    return result

# Test the function with the provided test case
assert convert_list_dictionary(
    ["S001", "S002", "S003", "S004"],
    ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],
    [85, 98, 89, 92]
) == [
    {'S001': {'Adina Park': 85}},
    {'S002': {'Leyton Marsh': 98}},
    {'S003': {'Duncan Boyle': 89}},
    {'S004': {'Saim Richards': 92}}
]

print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
    assert convert_list_dictionary(["abc","def","ghi","jkl"],["python","program","language","programs"],[100,200,300,400])==[{'abc':{'python':100}},{'def':{'program':200}},{'ghi':{'language':300}},{'jkl':{'programs':400}}]
    assert convert_list_dictionary(["A1","A2","A3","A4"],["java","C","C++","DBMS"],[10,20,30,40])==[{'A1':{'java':10}},{'A2':{'C':20}},{'A3':{'C++':30}},{'A4':{'DBMS':40}}]
