class Solution(object):
    def isValid(self, s):

        if (len(s) % 2 != 0):
            return False

        stack = []
        paranthesis = { "(":")", "[":"]", "{":"}" }

        for i in s:
            if (i in paranthesis):
                stack.append(i)
            else :
                if (len(stack) == 0):
                    return False
                if (paranthesis[stack[-1]] != i):
                    return False
                else :
                    stack.pop()

        if (len(stack) != 0):
            return False
        
        return True
