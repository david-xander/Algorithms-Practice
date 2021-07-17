
def main():
    data=[2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,9]
    # there must be an even number of edges in a graph
    if not sum(data)%2==0:
        raise RuntimeError("Not a graph sequence!!")
    print('HAVEL HAKIMI ', data)
    print(havelhakimi(data))

def havelhakimi(data):
    #
    # input: grade sequence
    # output: boolean... it is a graph or it is not
    #  
    data.sort()
    data.reverse()

    if not len(data)>0:
        return False
    
    first=data.pop(0)
    if first>0:
        if first>len(data):
            return False
        else:
            checkOK = True
            for key in range(0,first):
                data[key]-=1
                if data[key]<0:
                    checkOK=False
            if not checkOK:
                return False
            elif len(data)>0:
                return havelhakimi(data)
            elif data[0]==0:
                return True
            else:
                return False
    elif first==0:
        return True
    else:
        return False

if __name__ == "__main__":
    # execute only if run as a script
    main()