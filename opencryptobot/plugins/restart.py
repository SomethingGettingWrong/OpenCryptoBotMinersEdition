import os
import sys
import time
import opencryptobot.emoji as emo

from opencryptobot.plugin import OpenCryptoPlugin


class Restart(OpenCryptoPlugin):

    def get_cmd(self):
        return "restart"

    @OpenCryptoPlugin.only_owner
    @OpenCryptoPlugin.send_typing
    def get_action(self, bot, update, args):
        msg = f"{emo.WAIT} Bot is restarting..."
        update.message.reply_text(msg)

        time.sleep(0.2)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def get_usage(self):
        return None

    def get_description(self):
        return None