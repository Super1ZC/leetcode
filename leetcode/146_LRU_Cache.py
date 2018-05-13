import collections

class LRUCache:
    """一开始我想到的是双层字典，{0：{1：1}，1：{2：2}}这种样式
    让序列号在容量范围内变化，get方法，得到相应数据，并更新其count值
    put方法添加新的值并更新count值。
    然后看到讨论区很多人在用OrderedDict，将问题简化为超出容量时的更新直接将
    第一个元素（即LRU）丢出即可，最新的元素添加在字典的最后。"""
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #不存在对应key
        if not key in self.cache:
            return -1
        #先将这个键值对删除
        value = self.cache.pop(key)
        #再添加到字典的末端
        self.cache[key] = value
        #print(self.cache,'-'*2)
        return value
        
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #如果key存在，将键值对删除
        if key in self.cache:
            self.cache.pop(key)
        #如果字典的长度等于容量，且key不存在，删除字典中的第一个元素
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        #然后添加键值对
        self.cache[key] = value

        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
