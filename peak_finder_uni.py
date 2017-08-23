seqfile_name = "seq.txt"


def loadfile():
    print("Loading the sequence from file")
    with open(seqfile_name) as sf:
        array = []
        for line in sf:
            array += ([float(x) for x in line.split()])
    return array

def findpeak(seq, startind, finind, n):
    mid = (startind + finind)//2
    # print(startind, mid, finind)
    if (mid == 0) | ((seq[mid-1] <= seq[mid]) & (seq[mid] >= seq[mid+1])) | (mid == n):
        return mid
    elif (mid > 0) & (seq[mid-1] >= seq[mid]):
        return findpeak(seq, startind, mid, n)
    else:
        return findpeak(seq, mid+1, finind, n)

seq_test = loadfile()

# n = len(seq_test)
# print(n)
print(seq_test)
print(findpeak(seq_test, 0, n-1, n))
