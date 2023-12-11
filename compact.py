
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    def compact(lst)
    new_list= []
    for num in lst:
        if num == false:
         lst.pop(num)

def compact(lst):        
     return [val for val in lst if val]

     