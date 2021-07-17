
def main():
    data=[5,4,1,8,7,2,6,3]
    print('HARD WAY SORTING ', data, ': ', hardway(data))

def hardway(data):
    #
    # INPUT (list)
    # O(n**2)
    #
    res=[]
    for item in data:
        if len(res)==0:
            res.append(item)
        else:
            inserted=False
            for index, subitem in enumerate(res):
                if not inserted and item<subitem:
                    res.insert(index, item)
                    inserted=True
            
            if not inserted:
                res.append(item)
    return res

if __name__ == "__main__":
    # execute only if run as a script
    main()