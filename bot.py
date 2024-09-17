from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from token_manager import add_token, use_token, tokens_left


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

  def generate(update: Update, context: CallbackContext) -> None:
    token = add_token()
    update.message.reply_text(f'Your generated token is: {token}')

def check_tokens(update: Update, context: CallbackContext) -> None:
    remaining_tokens = tokens_left()
    update.message.reply_text(f'Tokens left: {remaining_tokens}')

def rename(update: Update, context: CallbackContext) -> None:
    if context.args and len(context.args) > 1:
        token = context.args[0]
        new_name = ' '.join(context.args[1:])
        if use_token(token):
            update.message.reply_text(f'Renaming to: {new_name}')
        else:
            update.message.reply_text('Invalid or expired token.')
    else:
        update.message.reply_text('Please provide a token and a new name.')
        
    def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("YOUR_BOT_TOKEN")

    dispatcher = updater.dispatcher

    # Register existing handlers
    dispatcher.add_handler(CommandHandler('rename', rename))  # Existing rename command
    dispatcher.add_handler(CommandHandler('generate', generate))  # New generate command
    dispatcher.add_handler(CommandHandler('tokens_left', check_tokens))  # New token count command

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
     
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()     
        print(f"{me.first_name} ɪꜱ ꜱᴛᴀʀᴛᴇᴅ.....⚡️")
        for id in Config.ADMIN:
            try: await self.send_message(id, f"**{me.first_name} ɪꜱ ꜱᴛᴀʀᴛᴇᴅ.....⚡️**")                                
            except: pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")

Bot().run()
