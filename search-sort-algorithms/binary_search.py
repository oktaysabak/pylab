# binary search
def ikili_arama(number_list: list, search: int):
    left = 0
    right = len(number_list)-1

    while(left<=right):
        mean = (left+right)//2
        if search == number_list[mean]:
            return mean
        elif search > number_list[mean]:
            # print(sol)
            left = mean + 1
        else:
            # print(sag)
            right = mean -1
        
    return -1


dizi = [5, 10, 11, 12, 13, 15, 26, 27, 34, 47]

indis = ikili_arama(dizi, 13)
print(indis)

