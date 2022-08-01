def get_sum(a,b):
    a_plus_b = a + b
    b_to_a = b
    a_to_b = a
    if a == b:
        return a
    elif a < b:
        while a != b:
            a += 1
            a_to_b += a
        return a_to_b
    else:
        while a != b:
            b += 1
            b_to_a += b
        return b_to_a

