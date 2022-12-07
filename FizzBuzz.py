class Solution(object):
    def fizzBuzz(self, n):
        i = []
        for j in range (1,n+1):
            if j%5==0 and j%3==0:
                i.append("FizzBuzz")
            elif j%3==0:
                i.append("Fizz")
            elif j%5==0:
                i.append("Buzz")
            else:
                i.append(str(j))
        return i
