import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5956738979:AAE5gMQXhG84PU33kg2kTABDnWK_DMzPbDo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message, res=False):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Факт")
    button2 = telebot.types.KeyboardButton("Стихотворение")
    button3 = telebot.types.KeyboardButton("Котики")
    button4 = telebot.types.KeyboardButton("Стикер")
    button5 = telebot.types.KeyboardButton('Рандомная игра')
    button6 = telebot.types.KeyboardButton('Игра по жанру')
    keyboard.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url = telebot.types.InlineKeyboardButton("Перейти", url='https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже', reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(message.chat.id, fact_link + fact_text)


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1, 10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHlR5j3jBsWL1vINHfIFfoF80W97IcngACoyIAAvOx-ErKIg00MiEaFi4E")



@bot.message_handler(commands=['gg'])
def send_game(message):
    response = requests.get('https://vgtimes.ru/games/top/').content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='game_search'))
    game_link = game.a.attrs['href']
    game_text = game.text
    bot.send_message(message.chat.id, game_link + game_text)


@bot.message_handler(commands=['genre'])
def send_genre(message, res=False):
    text_genre = 'Выбери жанр игры'
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Аркада")
    button2 = telebot.types.KeyboardButton("Хоррор")
    button3 = telebot.types.KeyboardButton("Гонки")
    button4 = telebot.types.KeyboardButton("Симулятор")
    button5 = telebot.types.KeyboardButton('Фэнтези')
    keyboard.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, text_genre, reply_markup=keyboard)


@bot.message_handler(commands=['Arcade'])
def send_genre_arcade(message):
    response = requests.get('https://vgtimes.ru/games/genres/arkada/#gb_top').content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='game_search_par'))
    game_link = game.a.attrs['href']
    game_text = game.text
    bot.send_message(message.chat.id, game_link + game_text)

@bot.message_handler(commands=['Horror'])
def send_genre_horror(message):
    response = requests.get('https://vgtimes.ru/games/genres/survival-horror/#gb_top').content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='game_search_par'))
    game_link = game.a.attrs['href']
    game_text = game.text
    bot.send_message(message.chat.id, game_link + game_text)

@bot.message_handler(commands=['Race'])
def send_genre_race(message):
    response = requests.get('https://vgtimes.ru/games/genres/gonki-vozhdenie/#gb_top').content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='game_search_par'))
    game_link = game.a.attrs['href']
    game_text = game.text
    bot.send_message(message.chat.id, game_link + game_text)

@bot.message_handler(commands=['Simulator'])
def send_genre_simulator(message):
    response = requests.get('https://vgtimes.ru/games/genres/simulyator/#gb_top').content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='game_search_par'))
    game_link = game.a.attrs['href']
    game_text = game.text
    bot.send_message(message.chat.id, game_link + game_text)

@bot.message_handler(commands=['Fantasy'])
def send_genre_fantasy(message):
    response = requests.get('https://vgtimes.ru/games/genres/fantasy/#gb_top').content
    html = BeautifulSoup(response, 'lxml')
    game = random.choice(html.find_all(class_='game_search_par'))
    game_link = game.a.attrs['href']
    game_text = game.text
    bot.send_message(message.chat.id, game_link + game_text)



@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.strip() == 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стихотворение':
        send_poem(message)
    elif message.text.strip() == 'Котики':
        send_cat(message)
    elif message.text.strip() == 'Стикер':
        send_sticker(message)
    elif message.text.strip() == 'Рандомная игра':
        send_game(message)
    elif message.text.strip() == 'Игра по жанру':
        send_genre(message)
    elif message.text.strip() == 'Аркада':
        send_genre_arcade(message)
    elif message.text.strip() == 'Хоррор':
        send_genre_horror(message)
    elif message.text.strip() == 'Гонки':
        send_genre_race(message)
    elif message.text.strip() == 'Симулятор':
        send_genre_simulator(message)
    elif message.text.strip() == 'Фэнтези':
        send_genre_fantasy(message)

bot.polling()