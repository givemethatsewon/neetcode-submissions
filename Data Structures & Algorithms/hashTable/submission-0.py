class Pair:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val


class HashTable:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None for _ in range(capacity)]
    
    def hash(self, key: int):
        index = 0
        for c in str(key):
            index += ord(c)

        return index % self.getCapacity()


    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
                    
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                
                return
            
            elif self.map[index].key == key:
                self.map[index].val = value 
                
                return
            
            index += 1
            index = index % self.capacity


    def get(self, key: int) -> int:
        index = self.hash(key)
        
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
            
        return -1



    def remove(self, key: int) -> bool:
        index = self.hash(key)
        if self.map[index] == None:
            return False
        
        self.map[index] = None
        self.size -= 1
        return True


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        
        newMap = []
        for _ in range(self.capacity):
            newMap.append(None)
        
        oldMap = self.map
        self.map = newMap
        
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.val)