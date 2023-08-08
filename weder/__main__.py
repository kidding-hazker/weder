import handlers

from aiogram.utils import executor
from bot import dispatcher
from shutil import rmtree

if __name__ == "__main__":
    executor.start_polling(dispatcher)
    rmtree("weder/__pycache__")