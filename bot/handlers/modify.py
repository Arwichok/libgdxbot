from aiogram import types as ats

from misc import dp
import keyboards as kb
from config import GROUP_ID
from models import Link


@dp.message_handler(commands='modify')
async def cmd_modify(msg: ats.Message):
    await msg.answer(
        'Delete/Edit links',
        reply_markup=await kb.modify_links()
    )

# TODO: edit links in future
# @dp.callback_query_handler(kb.edit_filter, is_chat_admin=GROUP_ID)
# async def edit(cq: ats.CallbackQuery, callback_data):
#     if not callback_data['id'].isdigit():
#         await cq.answer('Error id is not string')
#         return
#     link = Link.get(int(callback_data['id']))
#     print(callback_data)
#     await cq.answer()


@dp.callback_query_handler(kb.delete_filter, is_chat_admin=GROUP_ID)
async def delete(cq: ats.CallbackQuery, callback_data):
    if not callback_data['id'].isdigit():
        await cq.answer('Error id is not string')
        return
    link = await Link.get(int(callback_data['id']))
    if not link:
        await cq.answer('Link not found')
        return
    link_short = link.title[:10] + '... deleted'
    await link.delete()
    await cq.answer(link_short)
    await cq.message.edit_reply_markup(await kb.modify_links())
