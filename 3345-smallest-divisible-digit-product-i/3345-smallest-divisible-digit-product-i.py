class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+11):
            temp=i
            p=1
            while i>0:
                d=i%10
                p=p*d
                i=i//10
            if p%t==0:
                return temp
              

        