def max(data):
    max = 0
    for i in data:
        if i > max:
            max = i
    
    return max

def ram_sort(data):
    """ Project values to their index position then delete the gaps """
    """ Doesn't like floats """

    duplicates = []
    size = round(max(data))
    # create an array full of zeros at the size of the max value
    for i in range(size + 1):
        duplicates.append(0)

    # Project data elt to his index position and add it to the null array
    # if there is rounded duplicates, add the true value to a sub array
    for elt in data:
        e = round(elt)
        if duplicates[e] == 0:
            duplicates[e] = []
            duplicates[e].append(elt)
        else:
            inserted = False
            for i in range(len(duplicates[e])): # auto sort the sub array
                if elt < duplicates[e][i]:
                    duplicates[e].insert(i, elt)
                    inserted = True
                    break
            if not inserted:
                duplicates[e].append(elt)

    # remove all zeros and add values in the right order
    s_tab = []
    for elt in duplicates:
        if isinstance(elt, list):
            for i in range(len(elt)):
                s_tab.append(elt[i])
        elif elt != 0:
            s_tab.append(elt)
    
    return s_tab