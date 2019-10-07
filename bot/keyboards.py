from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IButton
from aiogram.utils.callback_data import CallbackData


from models import Link


modify_cd = CallbackData('m', 'action', 'id')
EDIT_ACTION = 'e'
DELETE_ACTION = 'd'
async def edit_filter(m): modify_cd.filter(action=EDIT_ACTION)
delete_filter = modify_cd.filter(action=DELETE_ACTION)


async def show_links():
    links = await Link.query.gino.all()
    kb = InlineKeyboardMarkup()
    for k in links:
        kb.add(IButton(text=k.title, url=k.url))
    return kb


async def modify_links():
    links = await Link.query.gino.all()
    kb = InlineKeyboardMarkup()
    for k in links:
        kb.add(
            IButton(text=k.title, url=k.url),
            # IButton('📝', callback_data=modify_cd.new(EDIT_ACTION, k.id)),
            IButton('❌', callback_data=modify_cd.new(DELETE_ACTION, k.id))
        )
    return kb
