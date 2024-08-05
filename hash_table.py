#yeh bilkul bhi samajh nahi aaya

class HashTable():
    def __init__(self, size = 7):
        self.data_map = [None] * size   #data_map is a list which is being created, it will create a list with seven elements in it and all of them contain none

    def __hash(self, key):
        my_hash = 0
        for i in key:
            my_hash = (my_hash + ord(i) * 23) % len(self.data_map)  #23 is prime so randomness is good, ratta maaro iska
        return my_hash  #will return value from 0 to 6

    def display(self):
        for i in self.data_map:
            print(i)

    def set_item(self, key, value):
        index = self.__hash(key)    #generates index and stores in index variable
        if self.data_map[index] == None:
            self.data_map[index] = []
        else:
            self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

h1 = HashTable()

h1.set_item("bolts", 1400)
h1.set_item("washers", 50)
h1.set_item("lumber", 70)

print(h1.get_item("washers"))
