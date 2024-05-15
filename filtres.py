from typing import Iterable

from aiogram.filters import Filter
from aiogram.types import Message


class IsAdmin(Filter):
    def __init__(self, admin_list: Iterable[int]) -> None:
        self.admin_list = admin_list

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_list
