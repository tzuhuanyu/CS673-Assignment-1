def combine(list_1, list_2):
    count = 0
    if len(list_1) - len(list_2) > 0:
        for_len = len(list_2)
        longer_len = len(list_1)
        wait_list = list_1

    elif len(list_1) - len(list_2) == 0:
        for_len = len(list_2)
        longer_len = len(list_2)
        wait_list = list_2 # useless
        count += 1
    else:
        for_len = len(list_1)
        longer_len = len(list_2)
        wait_list = list_2

    combined_list = []
    for i in range(0, for_len, 1):
        combined_list.append(list_1[i])
        combined_list.append(list_2[i])

    if count == 0:
        for i in range(longer_len-(longer_len-for_len),longer_len,1):
            combined_list.append(wait_list[i])

    print(combined_list)

list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]
list_3 = ['a', 'b', 'c','d','e','f','g']

combine(list_1, list_2)
combine(list_2, list_3)