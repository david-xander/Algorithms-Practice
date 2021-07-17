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