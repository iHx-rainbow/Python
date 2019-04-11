class RationalNumber:
    def __init__(self,numerator,denomiator):
        self._numerator=numerator
        self._denomiator=denomiator
    def convert2float(self):
        self._numerator=float(self._numerator)
        self._denomiator=float(self._denomiator)
    def __repr__(self):
        return "{}/{}".format(self._numerator,self._denomiator)
    def simplify(self):
        a=self._numerator
        b=self._denomiator
        while a%b!=0:
            a,b=b,(a%b)
        return(self._numerator/b,self._denomiator/b,)

a=RationalNumber(10,20)
print(repr(a))