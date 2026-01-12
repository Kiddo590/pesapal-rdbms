class HashIndex:
    def __init__(self):
        self.index = {}

    def add(self, key, pointer):
        if key in self.index:
            raise ValueError("Duplicate key violation")
        self.index[key] = pointer

    def get(self, key):
        return self.index.get(key)
