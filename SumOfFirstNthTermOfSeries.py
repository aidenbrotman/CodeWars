def series_sum(n):
    new_list = [1]
    denominator = 1
    if n == 1:
        new_list.append(format(1, ".2f"))
    else:
        while len(new_list) != n:
            denominator += 3
            new_list.append(format(float(new_list[-1]) + 1 / denominator, ".2f"))
    print(str(new_list[-1])

series_sum(0)
