def descending_order(num):
    if num == 0 or num > 0:  # checks for a positive input
        num_string = str(num)  # converts an integer to a string
        num_map = map(int, num_string)  # converts each character of num_string to an integer
        num_list = list(num_map)  # converts num_map to a list
        num_list.sort(reverse=True)  # sorts num_list in descending order
        num_list = [str(i) for i in num_list]  # converts each character of num_list to a string
        num_list = int("".join(num_list))  #  turns each character of num_list to an integer and turns num_list into an integer by joining the string indices
        print(num_list)

descending_order()