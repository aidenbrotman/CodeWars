def square_sum(numbers):
    square_list= []
    [square_list.append(n**2) for n in numbers]
    return sum(square_list)


square_sum([1, 2, 2])
