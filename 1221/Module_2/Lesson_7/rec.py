import speech_recognition as sr
import random

hello_list = ['Хай', 'Здарова', 'Добрый день']
film = ['Волк с Уолстрит', 'Титаник', 'Аватар', 'Человек паук']

recognizer = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь...")
        audio = recognizer.listen(source)

        speech = recognizer.recognize_google(audio, language="ru_RU")

        print(f"Вы сказали: {speech}")

        if speech.lower() == "привет":
            print(random.choice(hello_list))

        if speech.lower() == "фильм":
            print(random.choice(film))


