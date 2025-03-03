from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup # для работы состояний
from aiogram.dispatcher import FSMContext # тоже необходим для работы с состояниями
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # для работы с клавиатурой и кнопками



api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text= 'Рассчитать')
button2 = KeyboardButton(text= 'Информация')
kb.row(button1, button2)


@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст(целое число)')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age= int(message.text))
    await message.answer('Введите свой рост(целое число)')
    await UserState.growth.set()


@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = int(message.text))
    await message.answer('Введите свой вес(целое число)')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    form_calories = 10 * weight + 6.25 * growth - 5 * age - 161 # по формуле для женщин
    await message.answer(f'Суточная норма Ваших калорий составляет: {form_calories :.2f}')
    await state.finish()

@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Нажмите кнопку "Рассчитать"', reply_markup= kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать расчет")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
