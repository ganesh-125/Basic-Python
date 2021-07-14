def swap_element(list1,pos1,pos2):
    list1[pos1],list1[pos2] = list1[pos2],list1[pos1]
    print(list1)
list1 = [1,2,6,4,3]
swap_element(list1,0,-1)