class MyHashSet:

    def __init__(self):
        self.arr = []
        
    def add(self, key: int) -> None:
        if self.contains(key) == False:
            self.arr.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.arr.remove(key)

    def contains(self, key: int) -> bool:
        for val in self.arr:
            if key == val:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)