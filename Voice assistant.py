
#Голосовая озвучка
# import  os
# from pygame import mixer
# from gtts import gTTS
#
# my_file = open('some.txt', 'r', encoding='utf-8')
# my_string = my_file.read()
# my_file.close()
#
# mixer.init()
#
# tts = gTTS(text=my_string, lang='ru')
# tts.save('test.mp3')
# mixer.music.load('test.mp3')
# mixer.music.play()
# os.remove('test.mp3')

import pyaudio
import speech_recognition as sr
import random

r = sr.Recognizer()
while True:
    with sr.Microphone(device_index=1) as source:
        print('Скажи что-нибудь...')
        audio = r.listen(source)
    speech = r.recognize_google(audio, language='ru_RU').lower()
    print ('Вы сказали: ', speech)
    spisok = ['Привет', 'Здарова', 'Добрый день', 'Здравствуйте сэр', 'Ну как ты ковбой?', 'Пам пам пам, о здравствуйте сэр не заметила вас из-за музыки -)']
    spisok_films = ['Iron Man', 'Harry Potter', 'Grinch', 'Forest Gump', 'Blade Runner', 'Drive']
    if speech == 'привет':
        print(random.choice(spisok))
    if speech == 'фильм':
        print(random.choice(spisok_films))



