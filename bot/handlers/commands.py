from aiogram import types as ats
from aiogram.dispatcher import FSMContext

from misc import dp
import keyboards as kb
from config import GROUP_ID


@dp.message_handler(commands='start')
async def cms_start(msg: ats.Message):
    """
    Send welcome message.
    """
    await msg.answer(
        'LibGDX links',
        reply_markup=await kb.show_links()
    )


@dp.message_handler(commands='cancel', state='*')
async def cmd_cancel(msg: ats.Message, state: FSMContext):
    """
    Cancel all states.
    """
    if not await state.get_state():
        return
    await state.finish()
    await msg.answer('Canceled')


@dp.message_handler(commands='help', is_chat_admin=GROUP_ID)
async def cmd_help(msg: ats.Message):
    await msg.answer(
        "Add link /add\n"
        "/modify delete links"
    )
