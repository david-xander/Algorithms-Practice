class GradeSchoolNum():
    num = None
    text = None
    n = None

    def __init__(self, num) -> None:
        self.num = int(num)
        self.text = num
        self.n = len(self.text)
        
    def __mul__(self, other):
        res=0
        #
        # O(n*2n) = O(2n**2) = O(n**2)
        #
        for k in range(0, self.n):
            a=int(self.text[self.n-1-k])
            it=0
            for l in range(0, other.n):
                b=int(other.text[other.n-1-l])
                it += a * b * 10**l
            res += it * 10**k
        
        return res

    def __add__(self, other): 
        # Gradeschool adition
        return(self.num + other.num)

    def __sub__(self, other): 
        # Gradeschool substraction
        return(self.num - other.num)

class KaratsubaNum(GradeSchoolNum):
    a = ''
    b = ''

    def __init__(self, num) -> None:
        super().__init__(num)
        
        # n must be power of 2
        half=self.n//2
        if half>0:
            self.a=self.text[0:half]
            self.b=self.text[half:self.n]
    
    def __mul__(self, other):
        # n must be power of 2
        if self.n <= 1 or other.n <= 1:
            return(GradeSchoolNum(str(self.num))*GradeSchoolNum(str(other.num)))
        
        n = self.n
        a=KaratsubaNum(self.a)
        b=KaratsubaNum(self.b)
        c=KaratsubaNum(other.a)
        d=KaratsubaNum(other.b)
        p=KaratsubaNum(str(a+b))
        q=KaratsubaNum(str(c+d))
        ac=a*c
        bd=b*d
        pq=p*q
        adbc=pq-ac-bd

        return (ac * 10**n) + (adbc * 10**(n//2)) + bd
