def distance(strand_a, strand_b):
    dif=0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for i,char in enumerate(strand_b):
        if char!=strand_a[i]:
            dif+=1
    return dif
