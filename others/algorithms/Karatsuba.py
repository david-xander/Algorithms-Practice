from algorithms.GradeSchool import GradeSchoolNum

class KaratsubaNum(GradeSchoolNum):
    a = '0'
    b = '0'

    def __init__(self, num) -> None:
        super().__init__(num)
        
        # n must be power of 2
        half=self.n//2
        if half>0:
            self.a=self.text[0:half]
            self.b=self.text[half:self.n]
        else:
            self.b=self.text
    
    def __mul__(self, other):
        n = max(self.n, other.n)

        if n < 2:
            res=GradeSchoolNum(str(self.num))*GradeSchoolNum(str(other.num))
            return KaratsubaNum( str(res) )
        
        a=KaratsubaNum(self.a)
        b=KaratsubaNum(self.b)
        c=KaratsubaNum(other.a)
        d=KaratsubaNum(other.b)
        p=a+b
        q=c+d
        ac=a*c
        bd=b*d
        pq=p*q
        adbc=pq.num-ac.num-bd.num
        AC=ac.num * 10**n
        ADBC=adbc * 10**(n//2)
        BD = bd.num
        return KaratsubaNum( str( AC + ADBC + BD ))


    def __add__(self, other): 
        return KaratsubaNum(str(self.num + other.num))

    def __sub__(self, other): 
        return KaratsubaNum(str(self.num - other.num))