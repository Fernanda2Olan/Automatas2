#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import (
    ForceReply, 
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    )
from telegram.ext import (Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
)


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
    
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    logger.info(f"El usuario {user.first_name} ha iniciado una conversación.")
    await update.message.reply_html(
        rf"Hola {user.mention_html()}!, ¿en qué puedo ayudarte?",
        reply_markup=ForceReply(selective=True),
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    keyboard = [
        [InlineKeyboardButton('Horarios de las Tiendas', callback_data='Horarios')], 
        [InlineKeyboardButton('Venta de Cerveza', callback_data='Cerveza')],
        [InlineKeyboardButton('Horario de los Holanda', callback_data='Puestos')],
        [InlineKeyboardButton('¿Qué podré encontrar a la venta?', callback_data='Productos'),
        InlineKeyboardButton('Ubicaciones', callback_data='Ubicacion')]]
    menu_choices = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.message.chat_id, text="Opciones del Menú", reply_markup=menu_choices
    )
        
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Puedes usar el siguientes comando: 'Menú'. Para ver las opciones disponibles.")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton ('Las Ánimas', callback_data='De lunes a Miércoles de 7:00 am - 10:00 pm y de Jueves a Domingo 7:00 am a 12:00 am')]
    ]
    
    response_text = ""
    if query.data == "Horarios":
        response_text = "Te muestro los horarios: Las Animas, el Granero y el Molino de Lunes a Miércoles de 7:00 am a 10:00 pm y de Jueves a Domingo de 7:00 am a 12:00 am"
    elif query.data == "Cerveza":
        response_text = "Las 3 Tiendas tienen venta de cerveza, la venta comienza a las 10:00 am hasta el horario del cierre."
    elif query.data == "Puestos":
        response_text = "Los Holandas tienen un horario de 9:00 am a 7:00 pm, excepto el Holanda de la alberca de Olas y el del Canopy Tour ellos cierran a las 11:00 pm."
    elif query.data == "Productos":
        response_text = "En cualquiera de las 3 tiendas encontrarás todo lo necesario para tu visita: bolsas de hielo, carbón, cerveza fría, leña, aguas/sodas, café, cobijas, focos, todo lo esencial para que no te falte nada en tu acampado."

   

    # Send the response and show the menu again
    await query.message.reply_text(response_text)
    await menu(update, context)
        
    #await query.edit_message_text(text=f"Selected option: {query.data}")
    


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
        
    mensaje = update.message.text
    if mensaje.lower() == 'hola':
        mensaje = "Hola, ¿en qué puedo ayudarte?"
    elif mensaje.lower() == 'menú':
        await menu(update, context)
        return
    else:
        mensaje = "No entiendo tu mensaje. Usa 'Menú' para ver las opciones disponibles."

    await update.message.reply_text(mensaje)

def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7188374251:AAEj9DimUO9JzxVQWvpirrHmwiGkw1sVjoo").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("menu", menu))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(button))

    application.add_error_handler(error_handler)
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()