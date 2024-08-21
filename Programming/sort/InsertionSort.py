def InseretionSort(list):
    for slisticeEnd in range(len(list)):
        # build longer and longer sorted slices
        # in each iteration list[0:sliceEnd] a;ready sorted

        # move first element  after sorted slice left
        # till it is in the correct place
        pos = slisticeEnd
        while(pos>0 and list[pos] < list[slisticeEnd - 1]):
            (list[pos], list[pos - 1]) = (list[pos - 1], list[pos])
            pos = pos - 1