class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    
    def __init__(self, name, pet_type, owner = None) -> None:
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        if not (new_pet_type in self.PET_TYPES):
            raise ValueError('needs to be in PET_TYPES')
        self._pet_type = new_pet_type

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception('Must be type owner')
        self._owner = owner


class Owner:
    
    def __init__(self, name) -> None:
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('must be a type')
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name)