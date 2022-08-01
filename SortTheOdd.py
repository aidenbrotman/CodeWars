def sort_array(source_array):
    indices_array = []
    odd_array = []
    for y, x in enumerate(source_array):
        if x % 2 != 0:
            indices_array.append(y)
            odd_array.append(x)
    for index, replacement in zip(indices_array, sorted(odd_array)):
        source_array[index] = replacement
    print(source_array)







sort_array([5, 3, 2, 8, 1, 4])
