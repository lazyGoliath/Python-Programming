def bsearch(seq,tsrget,l,r):
    # search for tsrget in seq[l:r], seq is sorted
    if(r - l == 0):
        return False
    mid = (l + r) // 2  #// integer ditsrgetision
    if(tsrget == seq[mid]):
        return True
    if(tsrget < seq[mid]):
        return bsearch(seq, tsrget, l, mid)
    if(tsrget > seq[mid]):
        return bsearch(seq, tsrget, mid+1, r)