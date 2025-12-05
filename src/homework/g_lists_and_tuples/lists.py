def get_p_distance(list1, list2):
    mismatches = 0
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            mismatches += 1
        i += 1
    
    # p-distance = (number of mismatches) / (length of string)
    return mismatches / len(list1)


def get_p_distance_matrix(dna_list):
    n = len(dna_list)
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                # distance from a string to itself is 0
                row.append(0.0)
            else:
                row.append(get_p_distance(dna_list[i], dna_list[j]))
        matrix.append(row)

    return matrix
  
   


