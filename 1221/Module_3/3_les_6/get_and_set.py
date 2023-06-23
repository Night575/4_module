# class Year:
#     def __init__(self):
#         self.__days = 365
#
#     @property
#     def get_days(self):
#         return self.__days
#
#     @get_days.setter
#     def get_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise ValueError(f"Некорректное значчение атрибута: {days}")


# year = Year()
# print(Year.get_days)
# Year.get_days = 365
# print(Year.get_days)
# Year.get_days = 366


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
         if age < 0:
             raise ValueError("Вы еще не родились, пожылуйста покиньте сайт")

         self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    @property
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        del self.__name


person = Person("I", 16)
print(person.age)
person.age = 15
print(person.age)
person.age = -10