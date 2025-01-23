from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup # для работы состояний
from aiogram.dispatcher import FSMContext # тоже необходим для работы с состояниями
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # для работы с клавиатурой и кнопками
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton # для работы с инлайн клавиатурой



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

inl_kb = InlineKeyboardMarkup(resize_keybord=True)
inl_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data= 'calories')
inl_button2 = InlineKeyboardButton(text='Формулы расчета', callback_data= 'formulas')
inl_kb.row(inl_button1, inl_button2)

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup= inl_kb)


@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес(кг) + 6,25 х рост(см) - 5 х возраст(г) - 161' )
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст(целое число)')
    await call.answer()
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
    await message.answer('Привет, я бот помогающий твоему здоровью, нажмите "Рассчитать"', reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать расчет")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
