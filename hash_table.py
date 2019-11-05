class HashMap:

    def __init__(self):
        self.size = 2
        self.hash_map = [None] * self.size
        print(self.hash_map)

    def __hashing(self, key):
        slot = 0
        for i in str(key):
            slot += ord(i)
        return slot % self.size

    def set(self, key, val):
        address = self.__hashing(key)
        if self.hash_map[address] is None:
            self.hash_map[address] = []
        self.hash_map[address].append([key, val])
        return self.hash_map

    def get(self, key):
        address = self.__hashing(key)
        slot = self.hash_map[address]
        if slot is not None:
            for i in range(0, len(slot)):
                if slot[i][0] == key:
                    return slot[i][1]
        return f'No such a key'

    def keys(self):
        keys_array = []
        for i in range(0, len(self.hash_map)):
            if self.hash_map[i] is not None:
                keys_array.append(self.hash_map[i][0][0])
        return keys_array


table = HashMap()
print(table.set('grapes', 10000))
print(table.set('apples', 43))
print(table.set('pears', 31))
print(table.set('plums', 100))
value = table.get('grapes')
value = table.get('grapes')
value2 = table.get('peaches')
print(value2)
keys = table.keys()
print(keys)
