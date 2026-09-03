class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else: 
                cmin -= 1 
                cmax += 1  
            
            if cmax < 0:
                return False
            
            if cmin < 0:
                cmin = 0
                
        return cmin == 0
