# class A:
#     def info(self):
#         print("Это класс A")
#
#
#
# a = A()
# a.info()
#
#
# class B(A):
#     pass
#
#
# b = B()
# b.info()

class Pet:
    has_tail = True
    legs = 4
    name = None
    animal = None

    def __str__(self):
        result = f"Питомец {self.name}. Это {self.animal}. " \
                 f"У него {'есть хвост' if self.has_tail else 'хвоста нет'}. У него {self.legs} ног(и)."

        return result

    def sound(self):
        pass


class Dog(Pet):
    name = "Чарли"
    animal = "Собака"

    def sound(self):
        return "ГАВ!"

class Frog(Pet):
    has_tail = False
    name = "пепе"
    animal = "Лягушка"

    def sound(self):
        return "КВА!"


print(Frog(), Frog().sound())


# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
