class Pet:
    def __init__(self, has_tail, legs, name, animal):
        self.has_tail = has_tail
        self.legs = legs
        self.name = name
        self.animal = animal

    def __str__(self):
        result = f"Питомец {self.name}. Это {self.animal}. " \
                 f"У него {'есть хвост' if self.has_tail else 'хвоста нет'}. У него {self.legs} ног(и)."

        return result

    def sound(self):
        pass


class Dog(Pet):
    def __init__(self, has_tail, legs, name):
        super().__init__(has_tail, legs, name, "Собака")
