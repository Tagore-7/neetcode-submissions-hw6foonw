class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None 

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.hash_table = [None] * self.capacity

    def hash_function(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.hash_table[index]

        if not node:
            self.hash_table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.val = value 
                    return 
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.hash_table[index]

        while node:
            if node.key == key:
                return node.val 
            node = node.next 
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.hash_table[index]

        prev = None 
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next 
                else:
                    self.hash_table[index] = node.next
                self.size -= 1
                return True 
            prev, node = node, node.next 

        return False 

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity 

    def resize(self) -> None:
        new_capacity = 2 * self.capacity
        new_hash_table = [None] * new_capacity

        for node in self.hash_table:
            while node:
                index = node.key % new_capacity
                if new_hash_table[index] is None:
                    new_hash_table[index] = Node(node.key, node.val)
                else:
                    new_node = new_hash_table[index]
                    while new_node.next:
                        new_node = new_node.next 
                    new_node.next = Node(node.key, node. val)
                node = node.next 

        self.hash_table = new_hash_table
        self.capacity = new_capacity


