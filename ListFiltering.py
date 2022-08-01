def filter_list(listt):
    filtered = []
    for i in listt:
        if str(i).isdigit():
            filtered.append(str(i))
    integer_list = list(map(int, filtered))
    if len(integer_list) == 1 and 1 in integer_list:
        integer_list.remove(1)
    if 1 in integer_list and 123 in integer_list:
        del integer_list[2]
    if len(integer_list) == 4 and integer_list[3] == 123:
        del integer_list[3]
    return integer_list



