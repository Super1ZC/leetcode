class Solution():
    def addTwoNumbers(self,l1,l2):
        """这个是关于leetcode上面add two number的解法。有几个地方不是特别清楚"""
        carry = 0
        #不知道为什么这边要设两个值，其中n只是中间的变量，用于计算?
        root = n = ListNode(0)
        while l1 or l2 or carry:
            """这里面任一一个值不为空的时候循环"""
            #如果这个ListNode为空，自动赋值为0，用来计算
            x = y = 0
            if l1:
                x = l1.val
                #这个l1.next的操作应该是将这个值设为None，然后继续下一个值？
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            #这边用了divmod这个内置函数
            carry, val = divmod(x+y+carry,10)
            #这个不是很懂，在输入值？
            n.next = ListNode(val)
            #应该是给新的链表赋值。的吧
            n = n.next
        #因为n做了工作，然后root被补全了？不知道为什么n不行。
        return root.next
