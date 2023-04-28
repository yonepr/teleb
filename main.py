import telebot
from config import api
from telebot import types

bot = telebot.TeleBot(f"{api}")

@bot.message_handler(commands=['admin'])
def send_welcome(message):
	bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}!\nВы перешли в панель администратора.\nДля того что бы удостовериться, что это вы, пожалуйста введите пароль.".format(message.from_user))

@bot.message_handler(content_types='text')
def message_reply(message):
	if message.text == "12345678":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		add = types.KeyboardButton("Добавить")
		reset = types.KeyboardButton("Изменить")
		delete = types.KeyboardButton("Удалить")
		request = types.KeyboardButton("Запросить таблицу")
		opppen = types.KeyboardButton("Открыть шлагбаум")
		markup.add(add,reset,delete,request,opppen)
		bot.send_message(message.chat.id,"Вы полноценно зашли в панель администратора,вам открылись все возможности.",reply_markup=markup)

	elif message.text != "":
		bot.send_message(message.chat.id,"Неверный пароль, проверьте, что вы ввели его правильно.\nПопробуйте ещё раз.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("👋 Авторизация")
	btn2 = types.KeyboardButton("❓ Помощь")
	markup.add(btn1, btn2)
	bot.send_message(message.chat.id, text="Привет, {0.first_name}! 🚗 \n Данный бот позволяет открывать шлагбаум 😎, находящийся на территории КБО для сотрудников \"ТКС Саров 📞\"".format(message.from_user), reply_markup=markup)

	@bot.message_handler(content_types='text')
	def message_reply(message):
		if message.text=="👋 Авторизация":
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			phone_number = types.KeyboardButton("Отправить контакт", request_contact=True)
			btn2 = types.KeyboardButton("❓ Помощь")
			markup.add(phone_number, btn2)
			bot.send_message(message.chat.id,"Отправьте свой контакт для авторизации, пожалуйста. (Нажмите на кнопку)",reply_markup=markup)

		elif message.text=="❓ Помощь":
			bot.send_message(message.chat.id, "Для использования данного телеграм-бота пройдите этап авторизации, запросите пароль у Вашего администратора.\n После того как Вы авторизируйтесь, Вам откроются функции по открытию шлагбаума")

		@bot.message_handler(content_types=['contact'])
		def contact(message):
			if message.contact is not None:
				print(message.contact.phone_number)




bot.polling(none_stop=True)