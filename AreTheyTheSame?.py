def comp(array1, array2):
    new_list = []
    array1.sort()
    array2.sort()
    for a, b in zip(set(array1), set(array2)):
        print(set(array1))
        print(set(array2))
        if a ** 2 == b:
            print(True)
        elif a ** 2 != b:
            print(False)
            new_list.append(0)
    if new_list.count(True) == 8:
        print(True)
    elif set(new_list) == 0:
        print(False)

comp([121, 144, 19, 161, 19, 144, 19, 11],
     [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19])
comp([121, 144, 19, 161, 19, 144, 19, 11],
     [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19])
comp([121, 144, 19, 161, 19, 144, 19, 11],
     [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19])
