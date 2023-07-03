class Solution:
    def simplifyPath(self, path):
        stack = []
        for ele in path.split('/'):
            if stack and ele == '..':
                stack.pop()
            if ele != '..' and ele != '' and ele!='.':
                stack.append(ele)
            
        return '/'+'/'.join(stack)
            