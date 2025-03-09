from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8096033563:AAFJO1HPpcTy7cCQe1wwYXYz_TeeaDPswDo"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Каталог товаров (подписок)
products = {
    "1 месяц подписки": "499 рублей",
    "3 месяца подписки": "1299 рублей",
    "6 месяцев подписки": "2399 рублей"
}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = "👋 Добро пожаловать!\nВыберите подписку:\n"
    for item, price in products.items():
        text += f"\n📌 {item} – {price}"
    text += "\n\nОтправьте мне название подписки, чтобы продолжить."
    await message.answer(text)

@dp.message_handler(lambda message: message.text in products.keys())
async def select_product(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}.\n\nДля оформления заказа напишите 'Купить'.")

@dp.message_handler(lambda message: message.text.lower() == "купить")
async def checkout(message: types.Message):
    await message.answer("🛒 Оформление заказа...\n(После подтверждения ЮMoney тут появится оплата)")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)