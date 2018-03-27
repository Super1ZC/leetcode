import time
import functools


class Solution:
    """这是twoSum的解法，总的有三种，双循环暴力破解，快速排序后折半查找，和使用dict的的键值对进行操作。"""
    #想做成一个装饰器的，失败了。要在程序运行之后打印时间，貌似只能在返回函数之前做一些操作
    def time_used(self,func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            start = time.clock()
            print(time.clock()-start)
            return func(*args,**kw)
        return wrapper
    
    def twoSum1(self, nums, target):
        """This solution uses double loop and it's T(n)=O(n^2)"""
        start = time.clock()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    #Use print function to display the result
                    print([i,j])
        elapsed = (time.clock()-start)
        print('This solution uses: %s'%elapsed)
    
    def twoSum2(self, nums, target):
        """This solurion uses half-interval search and it's T(n)=O(nlogn)"""
        start = time.clock()
        sortedNum = sorted(nums)
        for i in sortedNum:
            rest = target - i
            low = 0
            high = len(nums)-1
            
            while(low<=high):
                mid = int((low+high)/2)
                if rest < sortedNum[mid]:
                    high = mid - 1
                    continue
                if rest > sortedNum[mid]:
                    low = mid + 1
                    continue
                if rest == sortedNum[mid]:
                    index1 = nums.index(i)
                    #这个操作是为了让【3，3】，这种情况的结果为【0，1】
                    nums[index1] = 'obtained'
                    index2 = nums.index(rest)
                    if index1>index2:
                        index1,index2 = index2,index1
                    #在leetcode里面，因为是return，所以会直接跳出循环，
                    #在这边因为用的是print函数，所以这个循环会一直存在，需要强制break
                    print([index1,index2])
                    break
            break
        print(time.clock()-start)
    
    def twoSum3(self,nums,target):
        """This solution uses dict and it's T(n)=O(n)"""
        start = time.clock()
        if len(nums)<= 1:
            return Flase
        d = {}
        for i in range(len(nums)):
            rest = target - int(nums[i])
            if rest in d:
                #d[rest] is one round before the i round.
                print([d[rest],i]) 
            else:
                d[nums[i]] = i
        print(time.clock()-start)
                
            
    def twoSum4(self, nums, target):
        """This solution uses dict but with enumerate function."""
        start = time.clock()
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                print([d[m], i])
            else:
                d[n] = i
        print(time.clock()-start)
    
    
                
nums = [3,2,4]
target = 6
s = Solution()
#s.twoSum1(nums,target)
#s.twoSum2(nums,target)
#s.twoSum3(nums,target)
s.twoSum4(nums,target)

