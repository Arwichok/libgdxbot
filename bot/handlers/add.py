from aiogram import types as ats
from aiogram.dispatcher import FSMContext

import keyboards as kb
from misc import dp
from models import Link
from states import AddLink
from config import GROUP_ID
import utils


@dp.message_handler(commands='add', is_chat_admin=GROUP_ID)
async def cmd_add(msg: ats.Message, state: FSMContext):
    """
    Start state AddLink is user is admin in @libgdx
    """
    await AddLink.url.set()
    await msg.answer("Send me URL, or /cancel")


@dp.message_handler(commands='add')
async def cmd_add_error(msg: ats.Message):
    """
    If user is not admin in @libgdx
    """
    await msg.answer("You are not admin in group @libgdx")


@dp.message_handler(state=AddLink.url)
async def add_url(msg: ats.Message, state: FSMContext):
    """
    Set URL to state
    """
    if await utils.url_status(msg.text) != 200:
        await msg.answer("URL is invalid")
        return

    await state.update_data(url=msg.text)
    await AddLink.title.set()
    await msg.answer(
        "Send link title \n"
        "/done for make title from site"
        "/cancel for cancel adding"
    )


@dp.message_handler(commands='done', state=AddLink.title)
async def done(msg: ats.Message, state: FSMContext):
    """
    Get title from url and save to DB
    """
    async with state.proxy() as proxy:
        title = await utils.get_url_title(proxy['url'])
        await Link.create(url=proxy['url'], title=title)

    await state.finish()
    await msg.answer(f"Link added")


@dp.message_handler(state=AddLink.title)
async def add_title(msg: ats.Message, state: FSMContext):
    """
    Get title from message and save to DB
    """
    async with state.proxy() as proxy:
        await Link.create(url=proxy['url'], title=msg.text)
        await msg.answer("Link added")
    await state.finish()
