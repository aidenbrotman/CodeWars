def find_it(seq):
    seq = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return seq[0]

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])

