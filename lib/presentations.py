import os
from abc import ABC, abstractmethod
from typing import Self

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

from lib import errors


class ViewManager:
    def __init__(self, bot: Bot | None = None):
        self.bot = bot
        if bot is None and (token := os.getenv("BOT_TOKEN")) is not None:
            bot = Bot(token=token)
        else:
            raise errors.BotTokenException("Bot token is not provided")

        self.clients: list = []
        self.dispatcher = Dispatcher()

    def handler(self, message: types.Message):
        if message.chat.id not in self.clients:
            self.clients.append(message.chat.id)


class View(ABC):
    def __init__(self, message: Message, bot: Bot):
        self.message = message
        self.bot = bot

    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def response(self) -> Self:
        pass


class StartView(View):
    def handle(self):
        print("StartView")
        self.message.answer("Hello, I'm a bot")

    def response(self) -> Self:
        return self
