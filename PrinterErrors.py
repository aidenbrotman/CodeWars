def printer_error(s):
    good_colors = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm')
    s_list = list(s)
    denominator = len(s_list)
    numerator = 0
    for x in s_list:
        if x not in good_colors:
            numerator += 1
    return f'{numerator}/{denominator}'