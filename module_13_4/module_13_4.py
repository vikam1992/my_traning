from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup 
from aiogram.dispatcher import FSMContext 



api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = 'Calories')
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

@dp.message_handler()
async def all_messages(message):
    await message.reply("Напишите 'Calories', чтобы начать расчет")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
