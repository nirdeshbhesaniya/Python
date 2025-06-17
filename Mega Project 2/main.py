import re
import asyncio
from markdownify import markdownify as md
import google.generativeai as genai
from config import GEMINI_API_KEY, TELEGRAM_BOT_TOKEN
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Store user prompts temporarily
user_prompts = {}

# Supported languages
LANGUAGES = ["python", "cpp", "java", "javascript", "c", "typescript", "html", "css", "php", "go", "swift"]

# Format Gemini response
def format_gemini_response(raw_text: str, language: str = "python") -> str:
    pattern = r"```(?:\w+)?\n(.*?)```"
    parts = re.split(pattern, raw_text, flags=re.DOTALL)
    formatted = ""

    def clean_and_format_explanation(text: str) -> str:
        markdown_text = md(text.strip())
        markdown_text = re.sub(r'[^\w\s.,:;!?()\[\]\'"“”\-]', '', markdown_text)
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', markdown_text) if len(s.strip()) > 25]
        sentences = sentences[:6]
        output = ""
        for idx, sentence in enumerate(sentences):
            match = re.match(r"([\w\s]{2,20}?):\s*(.*)", sentence)
            if match:
                topic = match.group(1).strip().capitalize()
                detail = match.group(2).strip()
                output += f"{idx+1}. *{topic}:* {detail}\n"
            else:
                output += f"{idx+1}. {sentence}\n"
        return output.strip()

    for i, part in enumerate(parts):
        if i % 2 == 0:
            explanation = clean_and_format_explanation(part)
            formatted += f"{explanation}\n\n"
        else:
            code = part.strip()
            formatted += f"```{language}\n{code}\n```\n\n"

    return formatted.strip()

# Generate AI response
def generate_response(prompt: str, language: str = "python") -> str:
    try:
        system_prompt = (
            f"Write a solution for the following request in {language}.\n"
            f"Include a clear explanation followed by properly formatted code inside triple backticks (```).\n"
            f"Prompt: {prompt}"
        )
        result = model.generate_content(system_prompt)
        return format_gemini_response(result.text, language)
    except Exception as e:
        return f"```{language}\n# Error: {str(e)}\n```"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 *Welcome to Code Generator Bot!*\n\n"
        "Send me any prompt like:\n"
        "`Create a login form in HTML`\n`Bubble sort in C++`\n\n"
        "Then pick a language.",
        parse_mode="Markdown"
    )

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    prompt = update.message.text
    user_prompts[user_id] = prompt

    async def clear_prompt():
        await asyncio.sleep(300)
        user_prompts.pop(user_id, None)

    context.application.create_task(clear_prompt())

    keyboard = [
        [InlineKeyboardButton(lang.title(), callback_data=f"{lang}|{user_id}")]
        for lang in LANGUAGES
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🧠 Choose a language to generate code:", reply_markup=markup)

# Handle language button press
async def handle_language_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        lang, user_id = query.data.split('|')
        user_id = int(user_id)
    except Exception:
        await query.edit_message_text("❌ Invalid selection.")
        return

    prompt = user_prompts.get(user_id)
    if not prompt:
        await query.edit_message_text("⚠️ Prompt expired. Please send again.")
        return

    waiting = await query.message.reply_text("⚙️ Generating response...")

    response_text = generate_response(prompt, lang)

    if len(response_text) > 4000:
        response_text = response_text[:3950] + "\n\n...truncated"

    try:
        sent = await query.message.reply_text(response_text, parse_mode="Markdown")
    except Exception:
        await query.message.reply_text("❌ Error formatting response. Try a simpler prompt.")
        return

    await asyncio.sleep(120)
    try:
        await context.bot.delete_message(chat_id=sent.chat_id, message_id=sent.message_id)
        await context.bot.delete_message(chat_id=waiting.chat_id, message_id=waiting.message_id)
    except Exception:
        pass

# Bot main loop
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_language_choice))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
