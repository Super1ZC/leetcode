class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                #顺序要小心，会影响除法的结果。
                r,l = int(stack.pop()),int(stack.pop())
                if i =='+':
                    stack.append(l+r)
                elif i=='-':
                    stack.append(l-r)
                elif i=='*':
                    stack.append(l*r)
                else:
                    #在python中6//-132 = -1，应该要0，所以这种情况要单独拎出来。
                    if l*r<0 and l%r !=0:
                        stack.append(l//r+1)
                    else:
                        stack.append(l//r)
        return int(stack[0])
