from aiogram.dispatcher.filters.state import State, StatesGroup


class AddLink(StatesGroup):
    url = State()
    title = State()


class EditLink(StatesGroup):
    id = State()
    new_title = State()
