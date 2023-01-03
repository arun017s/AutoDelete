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

from .info import * 
from pymongo import MongoClient

dbclient = MongoClient(DATABASE_URI)
db       = dbclient["Auto-Delete"]
col      = db["DATA"]

def save_message(message, time):
    data = {"chat_id": message.chat.id,
            "message_id": message.id,
            "time": time}
    col.insert_one(data)
   
def get_all_data(time):
    data     = {"time":{"$lte":time}}
    all_data = list(col.find(data))
    return all_data

def delete_all_data(all_data):
    for data in all_data:
        col.delete_one(data)
