class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                p_str = str1[:i]
                l1 = int(n1 / i)
                l2 = int(n2 /i)
                
                if (str1==p_str * l1) and (p_str * l2 == str2):
                    return p_str
                
        return ""


        