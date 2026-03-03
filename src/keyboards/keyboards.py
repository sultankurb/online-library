from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_keyboards(
        *buttons: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        sizes: tuple[int] = (2,),
):
    # 1. Use the specific ReplyKeyboardBuilder
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(buttons):
        # 2. Check for special button requests
        if request_contact is not None and index == request_contact:
            keyboard.add(KeyboardButton(text=text, request_contact=True))
        elif request_location is not None and index == request_location:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text))

    # 3. Adjust the grid and return the markup
    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True,
        input_field_placeholder=placeholder
    )