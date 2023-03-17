class Solution:
    """

    """
 #   method 1 - by simple recursion
    def findKthBit(self, n: int, k: int) -> str:
        def recur(i: int) -> str:
            def inverse(s):
                s = list(s)
                for i in range(len(s)):
                    if s[i] == '0':
                        s[i] = '1'
                    else:
                        s[i]='0'
                s = ''.join(s)
                return s[::-1]
            if i == 1:
                return '0'
            else:
                ans = recur(i-1)
                return ans + '1' + inverse(ans)
        str_ = recur(n)
        return str_[k-1]
    
#   method 2 - by finding pattern
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return '0'
        elif 2*k == (2**(n)):
            return '1'
        elif 2*k < (2**(n)):
            return self.findKthBit(n-1, k)
        else:
            return str(1 - int(self.findKthBit(n-1, (2**n)-k)))
        
        

    
