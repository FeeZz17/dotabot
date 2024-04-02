import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import dotenv_values
from aiogram import F
import random
from aiogram.filters.callback_data import CallbackData
from typing import Optional
from aiogram.utils.keyboard import InlineKeyboardBuilder
from heroes_index import (
    Ranged,
    Melee,
    Agility_Melee,
    Universal_Melee,
    Strength_Melee,
    Intellect_Ranged,
    Agility_Ranged,
    Universal_Ranged,
    Strength_Ranged,
)

config = dotenv_values(".env")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config["TG_TOKEN"])
# Диспетчер
dp = Dispatcher()


class AttackTypeChoice(CallbackData, prefix="AttackType"):
    attack_type: str


class PrimaryAttrChoice(CallbackData, prefix="PrimaryAttr"):
    attack_type: str
    primary_attr: str


class HeroChoice(CallbackData, prefix="Hero"):
    attack_type: str
    primary_attr: str
    id: int


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Выбор героя")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Выбор героя", reply_markup=keyboard)


@dp.message(F.text == "Выбор героя")
async def after(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Melee", callback_data=AttackTypeChoice(attack_type="Melee").pack()
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text="Ranged", callback_data=AttackTypeChoice(attack_type="Ranged").pack()
        )
    )

    builder.adjust(2)
    await message.answer("Выберите тип героя", reply_markup=builder.as_markup())


@dp.callback_query(AttackTypeChoice.filter())
async def attack_type_choice(
    callback: types.CallbackQuery, callback_data: AttackTypeChoice
):
    if callback_data.attack_type == "Melee":
        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(
                text="Agility ",
                callback_data=PrimaryAttrChoice(
                    attack_type="Melee", primary_attr="Agility"
                ).pack(),
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="Strength",
                callback_data=PrimaryAttrChoice(
                    attack_type="Melee", primary_attr="Strength"
                ).pack(),
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="Universal",
                callback_data=PrimaryAttrChoice(
                    attack_type="Melee", primary_attr="Universal"
                ).pack(),
            )
        )
    else:
        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(
                text="Agility",
                callback_data=PrimaryAttrChoice(
                    attack_type="Ranged", primary_attr="Agility"
                ).pack(),
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="Strength",
                callback_data=PrimaryAttrChoice(
                    attack_type="Ranged", primary_attr="Strength"
                ).pack(),
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="Universal",
                callback_data=PrimaryAttrChoice(
                    attack_type="Ranged", primary_attr="Universal"
                ).pack(),
            )
        )
        builder.add(
            types.InlineKeyboardButton(
                text="Intellect",
                callback_data=PrimaryAttrChoice(
                    attack_type="Ranged", primary_attr="Intellect"
                ).pack(),
            )
        )
    await callback.message.answer(
        f"Выберите главную характеристику {callback_data.attack_type} героя",
        reply_markup=builder.as_markup(),
    )
    await callback.answer()


@dp.callback_query(PrimaryAttrChoice.filter())
async def primary_type_choice(
    callback: types.CallbackQuery, callback_data: PrimaryAttrChoice
):
    builder = InlineKeyboardBuilder()
    if callback_data.attack_type == "Melee":
        if callback_data.primary_attr == "Agility":
            for i in Agility_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Melee", primary_attr="Agility", id=i["id"]
                        ).pack(),
                    )
                )
        elif callback_data.primary_attr == "Strength":
            for i in Strength_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Melee", primary_attr="Strength", id=i["id"]
                        ).pack(),
                    )
                )
        elif callback_data.primary_attr == "Universal":
            for i in Universal_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Melee", primary_attr="Universal", id=i["id"]
                        ).pack(),
                    )
                )
    if callback_data.attack_type == "Ranged":
        if callback_data.primary_attr == "Agility":
            for i in Agility_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Ranged", primary_attr="Agility", id=i["id"]
                        ).pack(),
                    )
                )
        elif callback_data.primary_attr == "Strength":
            for i in Strength_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Ranged", primary_attr="Strength", id=i["id"]
                        ).pack(),
                    )
                )
        elif callback_data.primary_attr == "Universal":
            for i in Universal_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Ranged", primary_attr="Universal", id=i["id"]
                        ).pack(),
                    )
                )
        elif callback_data.primary_attr == "Intellect":
            for i in Universal_Melee:
                builder.add(
                    types.InlineKeyboardButton(
                        text=i["name"],
                        callback_data=HeroChoice(
                            attack_type="Ranged", primary_attr="Intellect", id=i["id"]
                        ).pack(),
                    )
                )

    builder.adjust(3)
    await callback.message.answer(
        f"Выберите героя {callback_data.attack_type} {callback_data.primary_attr}",
        reply_markup=builder.as_markup(),
    )
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
