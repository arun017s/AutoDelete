# AutoDelete
Telegram bot to delete messages after specific time 
[![AutoDelete](https://te.legra.ph/file/e0e4b5df761aa6e9916b2.png)](https://github.com/arun017s/AutoDelete)

## Variables
1. `API_ID` : Get from [my.telegram.org](https://my.telegram.org)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your telegram bot token from [@BotFather](https://telegam.dog/BotFather)
4. `SESSION` : Generate from here [![Pyrogram Session](https://img.shields.io/badge/Pyrogram-812d13.svg?style=plastic&logo=Replit&logoColor=edd2a5)](https://replit.com/@Arun-TG/Pyrogram-Session)
5. `CHATS` : ID of Chats (seperate by spaces)
6. `TIME` : Time in seconds
7. `DATABASE_URI` : MongoDB URI, get from [mongodb.com](https://mongodb.com) (watch [video](https://youtu.be/HhHzCfrqsoE))
8. `WHITE_LIST` : messages from these users will not be deleted (User ID seperated by spaces) - Optional 
9. `BLACK_LIST` : only message from these users will be deleted (User ID seperated by spaces) - Optional 

## Branches
- ```main``` - Works with user account. It delete all types of messages  (```SESSION``` variable is required)
- ```bot-only``` - Works with bot. It does not delete messages coming from bots (```SESSION``` variable not required)

## Make sure: 
- Bot is admin in Chats with delete permission
- Account used to create `SESSION` is a member in Chats

## Deployment
You can fork and deploy this bot on any server (Render, Koyeb, Railway, Heroku.. etc)
<br>Remember to create variables!
<br>Some deployement options are mentioned below:

<details><summary>Koyeb</summary>
<br>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/arun017s/AutoDelete">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="deploy-to-koyeb">
</a>
<br>
Remember to create variables</details>

<details><summary>Railway</summary>
<br>
<a href="https://railway.app/new/template/mYFm9G?referralCode=Dxh7zU">
  <img src="https://railway.app/button.svg" alt="deploy-to-railway">
</a>
<br>
Remember to deploy the latest version</details>

<details>
<summary>VPS</summary>
Install latest version of <a href="python.org">Python</a>
Create variables approximately 
<pre>git clone https://github.com/arun017s/AutoDelete
cd AutoDelete
pip3 install -r requirements.txt
python3 main.py<pre>
</details>

## Support
Join in our Support Group for help & feedback
<br>
[![Telegram](https://img.shields.io/badge/Support%20Group-25a3e0.svg?logo=telegram&logoColor=ffffff)](https://telegram.dog/+kAphUpfIAllkYTE1)
[![Telegram](https://img.shields.io/badge/Update%20Channel-25a3e0.svg?logo=telegram&logoColor=ffffff)](https://telegram.dog/arun_tg)

## Note
🌠 Star & Fork the repo<br>
⚠️ Kangers stay back 

## Disclaimer
[![GNU General Public License v3.0](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/150px-GPLv3_Logo.svg.png)](https://www.gnu.org/licenses/gpl-3.0.html)    
Licensed under [GNU GPL v3.0](https://github.com/arun017s/AutoDelete/blob/main/LICENSE)<br>
Selling The Codes To Other People For Money Is *Strictly Prohibited*.


