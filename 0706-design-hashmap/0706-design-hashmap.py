class MyHashMap:

    def __init__(self):
        self.n = 10**6+1
        self.collections = [-1]*self.n

    def put(self, key: int, value: int) -> None:
        key%= self.n
        self.collections[key] = value


    def get(self, key: int) -> int:
        key%= self.n
        val = self.collections[key]
        return val

    def remove(self, key: int) -> None:
        key%= self.n
        self.collections[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)