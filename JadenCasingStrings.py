def to_jaden_case(string):
    print('Type a sentence to Jaden it.')
    string = input()
    string_list = string.split()  # turns string into list
    for i in range(len(string_list)):  # lowers and capitalizes each list item
        string_list[i] = string_list[i].lower().capitalize()
    joined_list = ' '.join(string_list)  # turns list into string
    print(joined_list)

to_jaden_case(input())
