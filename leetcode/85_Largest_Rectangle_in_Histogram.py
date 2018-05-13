class Solution:
    """用的还是堆栈"""
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #增加一位便于比较
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            #这个while循环很精髓，可以多次判断！我一开始就是只判断了一次然后死活算不出结果，理解不了这个算法。
            while heights[i]<heights[stack[-1]]:
                #这个pop操作很灵性，既得到了想要的值，又将stack更新了。
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                ans = max(ans,h*w)
            #放在外围，是为了不漏过每个细节
            stack.append(i)
        #这条语句不是必须的，但是复原了heights，显示了代码之美。
        heights.pop()
        return ans
