def dig_pow(n, p):
    n_list = list(str(n))
    my_list = []
    sum_my_list = 0
    k = 0
    for i in range(len(n_list)): # enumerates through
        check = int(n_list[i]) ** p
        p += 1
        my_list.append(check)
        sum_my_list = sum_my_list + my_list[i]  # to find sum of my_list elements
        k += 1
        return k if sum_my_list == (n * k) else -1

dig_pow(92, 1)
