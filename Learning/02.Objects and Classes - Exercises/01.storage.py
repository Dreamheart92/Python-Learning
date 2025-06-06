class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        storage_count = len(Storage.storage)

        if self.capacity > storage_count:
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage


storage = Storage(4)

storage.add_product("apple")

storage.add_product("banana")

storage.add_product("potato")

storage.add_product("tomato")

storage.add_product("bread")

print(storage.get_products())
