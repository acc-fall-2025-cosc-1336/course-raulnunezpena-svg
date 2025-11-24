def get_lowest_list_value(values):
    if len(values) == 0:
        return None
    lowest = values[0]
    
    lowest = values[0]
    i = 1
    while i < len(values):
        if values[i] < lowest:
            lowest = values[i]
        i += 1
    return lowest

def get_highest_list_value(values):
    if len(values) == 0:
        return None
    highest = values[0]
    
    i = 1
    while i < len(values):
        if values[i] > highest:
            highest = values[i]
        i += 1
    return highest