from telegram import Update  # Importa la clase Update, que representa cualquier mensaje o evento que recibe el bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# construye la aplicación del bot (ApplicationBuilder)
# maneja comandos como /start (CommandHandler)
# maneja mensajes normales ( MessageHandler)
# filtra tipos de mensajes (texto, comandos, etc.) ( filters)
# maneja el contexto de la conversación (ContextTypes)

TOKEN = 8995348778:AAGFHTzEV_ZkC7fjmhwwyVkoyx-Fw91-kQ4

# async = función asíncrona (Telegram trabaja con eventos en tiempo real)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update.message = mensaje recibido
    # reply_text = responde al usuario
    await update.message.reply_text(
        "ActiveDrybot.\n"
        
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Guarda el texto que escribe el usuario
    user_message = update.message.text

    # Responde al usuario con lo mismo que escribió
    await update.message.reply_text(
        f"Recibido: {user_message}"
    )

def main():
    # Crea la aplicación del bot usando el TOKEN
    app = ApplicationBuilder().token(TOKEN).build()

    # Registra el comando /start
    app.add_handler(CommandHandler("start", start))

    # Registra mensajes de texto normales (no comandos)
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    # Mensaje en consola para saber que el bot está activo
    print("🚀 Bot en ejecución... (CTRL + C para detenerlo)")

    # Mantiene el bot escuchando mensajes constantemente
    app.run_polling()
    
# Esto asegura que el bot solo arranque si ejecutás este archivo directamente
if __name__ == "__main__":
    main()    