def longest(a1, a2):
    new_list = (sorted(set(a1 + a2)))
    return "".join(new_list)





longest("aretheyhere", "yestheyarehere")