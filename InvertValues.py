def invert(lst):
    inverted_list = []
    for i in lst:
        if i * -1 < 0 or i * -1 > 0 or i == 0:
            inverted_list.append(i * -1)
    return inverted_list

invert([1, 2, 3, -4, -5])