class Solution
    """还有暴力破解法，时间复杂度为O（n^3），不会写，也没人写。有兴趣的可以直接在这道题里面的solution找到原理讲解
    还有一种方法叫sliding window。时间复杂度为O（n^2）。我就了解了一下。毕竟还没工作，往下多学学再说。"""
    def lengthofLongestSubstring(self,s):
        """这个方法的时间复杂度为O（n），对整个字符串检索一遍，将独特的
        字符放到临时的字典里面，下次再遇到时，直接跳过。"""
        #这个空字典用来存放第一次出现的字符
        used = {}
        start = maxlength = 0
        
        for index,value in enumerate(s):
            #如果字符重复了并且起始值不小与当前字符的序列（'tmmzuxt'防止这种情况结果为4）
            if s[index] in used and start<=used[value]:
                #两个数重复，取后一位起始'tmmzuxt'中取第二个m当初start。
                start = used[value]+1
            else:
                #将原来的最大长度与新的最大长度比较。
                maxlength = max(maxlength,index-start+1)
            used[value] = index
        return maxlength
                
