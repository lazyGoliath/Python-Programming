def SelectionSort(l):
    #scan slices [0, len], [1, len(l)], ....
    for start in range(len(l)):
        #find minimum pos in slice ...
        minpos = start  #assume
        for i in range(start, len(l)):
            if(l[i] < l[minpos]):
                minpos = i
        #swap
        (l[minpos], l[start]) = (l[start], l[minpos])
