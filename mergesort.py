import math

def main():
    data=[10, 5, 12, 4, 1, 8, 2, 11, 7, 9, 13, 3, 6, 14]
    print('MERGESORT ', data, ': ', merge_sort(data))

res = []
def merge_sort(data):
    n=len(data)
    half=n//2
    
    L=data[0:half]
    R=data[half:n]
    
    if len(L)>1:
        L=merge_sort(L)
    if len(R)>1:
        R=merge_sort(R)    

    res=merge_ordered(L,R)

    return res

def merge_ordered(L, R):
    res=[]
    while len(L)>0 and len(R)>0:
        if L[0]<R[0]:
            res.append(L[0])
            L.pop(0) # Damm!!! I just realized pop(i) is O(n), so this is bad!!
        else:
            res.append(R[0])
            R.pop(0) # Same!!! Shame on me!
    
    for item in L:
        res.append(item)
    for item in R:
        res.append(item)
    
    return res

if __name__ == "__main__":
    # execute only if run as a script
    main()