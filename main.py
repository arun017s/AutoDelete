#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

from time import time 
from utils.info import *
from utils.database import *
from subprocess import Popen
from pyrogram import Client, filters

User = Client("auto-delete-user",
              session_string=SESSION)

@User.on_message(filters.chat(CHATS))
async def delete(user, message):
    try:
       if bool(WHITE_LIST):
          if message.from_user.id in WHITE_LIST:
             return 
       if bool(BLACK_LIST):
          if message.from_user.id not in BLACK_LIST:
             return
       _time = int(time()) + TIME 
       save_message(message, _time)
    except Exception as e:
       print(str(e))

@User.on_message(filters.regex("!start") & filters.private)
async def start(user, message):
    await message.reply("Hi, I'm alive!")

#==========================================================

Popen(f"gunicorn utils.server:app --bind 0.0.0.0:{PORT}", shell=True)
Popen("python3 -m utils.delete", shell=True)
User.run()
