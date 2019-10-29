def add_two_largest(a_list):
    '''(list) -> number

    Returns the addition of the two largest numbers in a list received as argument.
    '''
    max1 = max(a_list)
    index_max1 = a_list.index(max1)
    a_list.remove(max1)
    max2 = max(a_list)
    MAX = max1 + max2
    a_list.insert(index_max1, max1)
    return MAX
    
