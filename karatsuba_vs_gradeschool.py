from algorithms.Karatsuba import KaratsubaNum, GradeSchoolNum

def main():
    #
    # ONLY WORKS with same n in x and y
    #
    x=KaratsubaNum('1211')
    y=KaratsubaNum('1111')
    res=x*y
    print("Karatsuba: ",res)
    x=GradeSchoolNum('1211')
    y=GradeSchoolNum('1111')
    res=x*y
    print("GradeSchool: ",res)

if __name__ == "__main__":
    # execute only if run as a script
    main()