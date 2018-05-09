class Solution1:
    """这个方法用了堆栈。设定（）的绝对值为1，[]的绝对值为2，{}的绝对值为3。"""
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {'(':1,')':-1,'[':2,']':-2,'{':3,'}':-3}
        for i in s:s
            #是],),}的情况。d[i]<0可以不要，但是会降低整体效率。可能是因为会产生额外的计算费用
            if stack and (d[i]<0 and d[i]+d[stack[-1]]==0):
                #精髓的一步，将配对成功的符号移除。
                stack.pop()
            else:#以（，[,{打头
                stack.append(i)
        #正常的情况下()[]，一进一出，一进一出，最后stack为空。其余都是错误的
        return stack == []
        
class Solution2:
    """也是堆栈"""
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
