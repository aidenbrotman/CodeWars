def DNA_strand(dna):
    dna_list = list(dna)
    new_string = []
    for i in dna_list:
        if i == 'A':
            replacement = i.replace('A', 'T')
            new_string.append(replacement)
        elif i == 'T':
            replacement = i.replace('T', 'A')
            new_string.append(replacement)
        elif i == 'C':
            replacement = i.replace('C', 'G')
            new_string.append(replacement)
        elif i == 'G':
            replacement = i.replace('G', 'C')
            new_string.append(replacement)
    return "".join(new_string)

def DNA_strand(dna):
    dna_list = list(dna)
    new_string = []
    for i in dna_list:
        if i == 'A':
            new_string.append(i.replace('A', 'T'))
        elif i == 'T':
            new_string.append(i.replace('T', 'A'))
        elif i == 'C':
            new_string.append(i.replace('C', 'G'))
        elif i == 'G':
            new_string.append(i.replace('G', 'C'))
    return "".join(new_string)