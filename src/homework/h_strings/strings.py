def get_hamming_distance(dna1, dna2):
    # Assumes dna1 and dna2 are the same length
    distance = 0

    i = 0
    while i < len(dna1):
        if dna1[i] != dna2[i]:
            distance += 1
        i += 1

    return distance


def get_dna_complement(dna):
    # This is the REVERSE complement:
    # reverse the string, then complement each base.

    result = ""
    i = len(dna) - 1  # start from last index (no slicing)

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
            # if unexpected character, keep it as-is (or you could raise an error)
            result += base

        i -= 1

    return result
