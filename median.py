def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        # odd number of elements
        index = len(sorted_list) // 2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        # even no. of elements
        m = 0
        for i in sorted_list:
            m += i
            #print (m)
        med = m / len(sorted_list)
        return med


print (median([2, 4, 6, 9]))