class Solution:
    def maxProduct(self, n: int) -> int:
        p=1
        digits=[]
        while(n>0):
            d=n%10
            digits.append(d)
            n=n//10
        digits.sort(reverse=True)
        return digits[0]*digits[1]
        