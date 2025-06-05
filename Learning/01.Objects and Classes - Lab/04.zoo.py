class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species: str):
        names = []
        species_type = ''

        if species == 'mammal':
            names = self.mammals
            species_type = 'Mammals'
        elif species == 'fish':
            names = self.fishes
            species_type = 'Fishes'
        elif species == 'bird':
            names = self.birds
            species_type = 'Birds'

        return (f"{species_type} in {self.name}: {', '.join(names)}\n"
                f"Total animals: {self.__animals}")


zoo_name = input()
zoo = Zoo(zoo_name)

loop_end = int(input())

for i in range(loop_end):
    species, name = input().split(' ')
    zoo.add_animal(species, name)

species_type = input()

print(zoo.get_info(species_type))
