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

import asyncio 
from . import * 
from time import time 
from pyrogram import Client, idle 
#-------------------------------------------------------------------------------
bot = Client("auto-delete-bot-2",
          api_id=API_ID,
          api_hash=API_HASH,
          bot_token=BOT_TOKEN)
#-------------------------------------------------------------------------------

async def check_up(bot):   
    _time = int(time()) 
    all_data = get_all_data(_time)
    for data in all_data:
        try:
           await bot.delete_messages(chat_id=data["chat_id"],
                               message_ids=data["message_id"])           
        except Exception as e:
           err=data
           err["Error"]=str(e)
           print(err)
    delete_all_data(all_data)

async def run_check_up():
    async with bot:     
        while True:  
           await check_up(bot)
           await asyncio.sleep(1)
    
if __name__=="__main__":   
   asyncio.get_event_loop().run_until_complete(run_check_up())
