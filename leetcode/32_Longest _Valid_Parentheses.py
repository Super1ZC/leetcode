class Solution1:
    """DP解法，挺快的"""
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0
        for i in s:
            if i =='(':
                stack.append(0)
            else:
                if len(stack)>1:
                    val = stack.pop()
                    stack[-1] += val+2
                    longest = max(longest,stack[-1])
                else:
                    stack[0] = 0
        return longest

class Solution2:
    """用stack做的"""
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        longest = 0
        leftmost = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    leftmost = i
                else:
                    #事先将')'的index剔除，然后根据情况来判断
                    stack.pop()
                    #栈为空，说明前面没有多余的'('
                    if not stack:
                        longest = max(longest,i-leftmost)
                    #栈不为空，用最后一个'('所在的index计算
                    else:
                        longest = max(longest,i-stack[-1])
        return longest
