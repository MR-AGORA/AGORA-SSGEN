from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}, 
Welcome to {}

You Can Use This Bot To Generate Pyrogram & Telethon String Session. Use Below Buttons To Operate !

**Made With Love By @Mr_Agora and @Agora_Robots ❤️**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💫 START GENERATING AGORA SESSION 💫", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("💫 START GENERATING AGORA SESSION 💫", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("💫 START GENERATING AGORA SESSION 💫", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About 🚀", callback_data="about")
        ],
        [InlineKeyboardButton("❣️ Contact Owner ❣️", url="https://t.me/mr_agora")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/start - Start The Bot
/help - Help Message
/generate - Generate String Session
/cancel - Cancel The Process
/about - About Bot
"""

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Generate Pyrogram & Telethon String Sessions. 

Made With ❤ By @Mr_Agora and @Agora_Robots

Sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Agora_Robots)

Fʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

Lᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

Dᴇᴠᴇʟᴏᴘᴇʀ : [ΛႺՕ𝖱Λ](https://t.me/mr_agora)
    """
