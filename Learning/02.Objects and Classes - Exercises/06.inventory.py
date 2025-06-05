class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        items_count = len(self.items)

        if items_count < self.__capacity:
            self.items.append(item)
            return None
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ', '.join(self.items)
        capacity_left = self.__capacity - len(self.items)

        return f"Items: {items}.\nCapacity left: {capacity_left}"


inventory = Inventory(2)

inventory.add_item("potion")

inventory.add_item("sword")

print(inventory.add_item("bottle"))

print(inventory.get_capacity())

print(inventory)
