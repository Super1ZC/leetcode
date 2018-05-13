class Solution1:
    """DP解法，感觉还能改进"""
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left = []
        right = []
        h1 = 0
        h2 = 0
        #从左往右
        for i in range(len(height)):
            if height[i]>h1:
                h1 = height[i]
            left.append(h1-height[i])
        #从右往左
        for j in range(len(height)-1,-1,-1):
            if height[j]>h2:
                h2 = height[j]
            right.append(h2-height[j])
        #print(left)
        #print(right)
        #为了计算方便，有需要可以打印left，right看看具体情况。
        right.reverse()
        #print(right)
        for x in range(len(height)):
            ans += min(left[x],right[x])
        return ans
        
class Solution2:
    """未完成的stack解法，应该是计算横向的储水量。但是有点搞不懂里面的逻辑。"""
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                top = stack.pop()
                distance = i-top
                print(distance,'+'*2)
                bounded_height = height[i]-height[top]
                print(bounded_height,'-')
                ans += distance*bounded_height
                print(ans,'*'*2)
            stack.append(i)
        return ans

class Solution3:
    """双指针移动法，在python中效率最高"""
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #连续赋值比一个个赋值效率要高，不懂为什么
        l,r,ans,min_height = 0,len(height)-1,0,0
        #循环条件，左指针要小于右指针
        while l < r:
            while l < r and height[l]<=min_height:
                ans += min_height - height[l]
                l +=1
            while r > l and height[r]<=min_height:
                ans += min_height - height[r]
                r -=1
            min_height = min(height[l],height[r])
        return ans
