from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application, MessageHandler, filters

TOKEN: Final = "YOUR_BOT_TOKEN" # Replace with your bot token

BOT_USERNAME: Final = "YOUR_BOT_USERNAME" # Replace with your bot username(Remember to include '@' symbol before the username)

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I'm ki1n's bot!")

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if "hello" in processed:
        return "Hiya!"
    
    if "how are you" in processed:
        return "I'm doing great! Thanks for asking!"
    
    if "goodbye" in processed:
        return "Goodbye! Have a great day!"
    
    return "I'm sorry, I don't understand!"

# Handle messages in groups
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return 
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
        
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)
    

