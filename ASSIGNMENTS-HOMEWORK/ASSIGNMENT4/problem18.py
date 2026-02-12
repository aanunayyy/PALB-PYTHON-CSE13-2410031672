class Solution:
    def factorial(self, n):
        result = 1
        
        for i in range(2, n + 1):
            result *= i
        
        return [int(d) for d in str(result)]
