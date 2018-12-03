import inspect

from telegram import ChatAction
from opencryptobot.config import ConfigManager as Cfg


class OpenCryptoPlugin:

    def __init__(self, updater, db):
        self.updater = updater
        self.db = db

    @classmethod
    def send_typing(cls, func):
        def _send_typing_action(self, bot, update, **kwargs):
            if update.message:
                user_id = update.message.chat_id
            else:
                user_id = update.callback_query.message.chat_id

            bot.send_chat_action(
                chat_id=user_id,
                action=ChatAction.TYPING)

            return func(self, bot, update, **kwargs)
        return _send_typing_action

    @classmethod
    def only_owner(cls, func):
        def _only_owner(self, bot, update, **kwargs):
            if Cfg.get("admin_id") == update.effective_user.id:
                return func(self, bot, update, **kwargs)

        return _only_owner

    @classmethod
    def save_data(cls, func):
        def _save_data(self, bot, update, **kwargs):
            if Cfg.get("use_db"):
                usr = update.message.from_user

                if not self.db.user_exists(usr.id):
                    self.db.add_user(usr)

                self.db.save_cmd(usr.id, update.message.text)

            return func(self, bot, update, **kwargs)
        return _save_data

    def get_cmd(self):
        method = inspect.currentframe().f_code.co_name
        raise NotImplementedError(f"Interface method '{method}' not implemented")

    def get_action(self, bot, update, args):
        method = inspect.currentframe().f_code.co_name
        raise NotImplementedError(f"Interface method '{method}' not implemented")

    def get_usage(self):
        method = inspect.currentframe().f_code.co_name
        raise NotImplementedError(f"Interface method '{method}' not implemented")

    def get_description(self):
        method = inspect.currentframe().f_code.co_name
        raise NotImplementedError(f"Interface method '{method}' not implemented")