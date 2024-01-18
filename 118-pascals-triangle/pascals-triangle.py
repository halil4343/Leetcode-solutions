class Solution:
    
    def generate(self, numRows: int):
        
        
        
        
        
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
        
        
        
        
        def combination(n: int):
            liste = []
            for r in range(0,n+1):
                comb = factorial(n)/(factorial(r)*factorial(n-r))
                liste.append(int(comb))
            return liste
                
        
        
        liste = []
        for i in range(numRows):
            row = combination(i)
            liste.append(row)
        return liste