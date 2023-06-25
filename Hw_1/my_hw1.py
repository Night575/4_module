word = input("Введите слово: ")

if word.lower() == word.lower()[::-1]:
    print("Полиндром")
else:
    print("Не полиндром")