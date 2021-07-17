
def main():
    data=[5,4,1,8,7,2,6,3]
    print('MERGESORT ', data, ': ', mergesort(data))

res = []
def mergesort(data):
    n=len(data)
    half=n//2
    
    p1=data[0:half]
    p2=data[half:n]
    
    if len(p1) > 1:
        mergesort(p1)

    if len(p2) > 1:
        mergesort(p2)

    if p1[0]<=p2[0]:
        res.append(p1[0])
        res.append(p2[0])
    else:
        res.append(p2[0])
        res.append(p1[0])

    return res

if __name__ == "__main__":
    # execute only if run as a script
    main()