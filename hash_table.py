class HashMap:
    '''
    Constructor with default any size
    '''
    def __init__(self,size):
        self.size = size
        self.hash_map = [None] * self.size
        print(self.hash_map)
     
    '''
    I created hashing private method where it returns slot for accessing/modifying our <key>,<values>
    '''
    def __hashing(self, key) -> int:
        slot = 0
        for i in str(key):
            slot += ord(i)
        return slot % self.size
    
    '''
    Here we can add <key>/<value> entry to our HashMap
    '''
    def set(self, key, val) -> List[int]:
        address = self.__hashing(key)
        if self.hash_map[address] is None:
            self.hash_map[address] = []
        self.hash_map[address].append([key, val])
        return self.hash_map
    
    '''
    This function will return the value of the corresponding key
    '''
    def get(self, key)->int:
        address = self.__hashing(key)
        slot = self.hash_map[address]
        if slot is not None:
            for i in range(0, len(slot)):
                if slot[i][0] == key:
                    return slot[i][1]
        return f'No such a key'
    
    '''
    This function will return array of keys in the HashMap
    '''
    def keys(self) -> []:
        keys_array = []
        for i in range(0, len(self.hash_map)):
            if self.hash_map[i] is not None:
                keys_array.append(self.hash_map[i][0][0])
        return keys_array
    '''
    This function will return only array of values
    '''
    def values(self) -> []:
        values_array = []
        for i in range(0, len(self.hash_map)):
            if self.hash_map[i] is not None:
                values_array.append(self.hash_map[i][0][1])
        return values_array
    
    '''
    This function will return list of tuples(<key>,<value>)
    '''
    def key_value(self) -> []:
        values_key_array = []
        for i in range(0, len(self.hash_map)):
            if self.hash_map[i] is not None:
                values_key_array.append((self.hash_map[i][0][0],self.hash_map[i][0][1]))
        return values_key_array


table = HashMap(2)
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
values = table.values()
print(values)
keys_values = table.key_value()
print(keys_values)
