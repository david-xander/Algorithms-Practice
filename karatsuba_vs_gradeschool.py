from algorithms.Karatsuba import KaratsubaNum, GradeSchoolNum

def main():
    num1 = '5678'
    num2 = '1234'

    #
    # ONLY WORKS with same n in x and y
    #
    x=KaratsubaNum(num1)
    y=KaratsubaNum(num2)
    res=x*y
    print("Karatsuba: ",res.num)
    x=GradeSchoolNum(num1)
    y=GradeSchoolNum(num2)
    res=x*y
    print("GradeSchool: ",res)

if __name__ == "__main__":
    # execute only if run as a script
    main()