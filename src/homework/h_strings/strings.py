def get_hamming_distance(dna1, dna2):
   
    distance = 0

    i = 0
    while i < len(dna1):
        if dna1[i] != dna2[i]:
            distance += 1
        i += 1

    return distance


def get_dna_complement(dna):
    

    result = ""
    i = len(dna) - 1  

    while i >= 0:
        base = dna[i]

        if base == 'A':
            result += 'T'
        elif base == 'T':
            result += 'A'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
        else:
            
            result += base

        i -= 1

    return result
