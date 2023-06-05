def selection_sort(seq,order=1):
    if order==1:
        for i in range(len(seq)-1):
            id_new = seq.index(min(seq[i:]))
            seq[i],seq[id_new] = seq[id_new],seq[i]
    else:
        for i in range(len(seq)-1):
            id_new = seq.index(max(seq[i:]))
            seq[i],seq[id_new] = seq[id_new],seq[i]

    return seq

print(selection_sort([4,8,9,1,3,2],0))