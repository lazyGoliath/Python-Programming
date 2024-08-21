def QuickSort(A,l,r):  #Sort A[l:r]
    if r-l <= 1:   #base case
        return ()
    
    # partition with respect to pivot, a[l]
    yellow = l+1
    for green in range(l+1,r):
        if A[green] <= A[l]:
            (A[green], A[yellow]) = (A[yellow], A[green])
            yellow += 1
    
    # move pivot into place
    (A[l], A[yellow-1]) = (A[yellow-1], A[l])

    QuickSort(A, l, yellow-1)  #recursive calls
    QuickSort(A, yellow, r)