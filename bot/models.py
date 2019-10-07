from gino import Gino
from aiogram import Dispatcher

from config import DB_URL
from misc import executor


db = Gino()


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String())
    title = db.Column(db.Unicode())


@executor.on_startup
async def on_startup(dp: Dispatcher):
    await db.set_bind(DB_URL)
    await db.gino.create_all()


@executor.on_shutdown
async def on_shutdown(dp: Dispatcher):
    await db.pop_bind().close()
