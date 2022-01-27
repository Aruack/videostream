# Copyright (C) 2021 By MarrkMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ __Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !__\n
💭 __[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ's ᴠɪᴅᴇᴏ ᴄʜᴀᴛs!__

💡 __Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚 Cᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!__

🔖 __🔖 ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ, ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ » ❓ ʙᴀsɪᴄ ɢᴜɪᴅᴇ ʙᴜᴛᴛᴏɴ!__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("ʙᴀsɪᴄ ɢᴜɪᴅᴇ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbcmds"),
                    InlineKeyboardButton("ᴄʀᴇᴀᴛᴏʀ", url=f"https://t.me/Aruack"),
                ],
                [
                    InlineKeyboardButton(
                        "ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Araucksupport"
                    ),
                    InlineKeyboardButton(
                        "ʙᴏᴛ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/aruackofficial"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ __Basic Guide for using this bot:__

1.) __First, add me to your group.__
2.) __Then, promote me as administrator and give all permissions except Anonymous Admin.__
3.) __After promoting me, type /reload in group to refresh the admin data.__
3.) __Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.__
4.) __Turn on the video chat first before start to play video/music.__
5.) __Sometimes, reloading the bot by using /reload command can help you to fix some problem.__

📌 __If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.__

💡 __If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}__

⚡ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} **""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ __Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !__

» __Click the button below to see the list of commands !__

⚡ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("sᴜᴅᴏ ᴄᴍᴅ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ʙᴀsɪᴄ ᴄᴍᴅ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙ɢᴏ ʙᴀᴄᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /play (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} **""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} **""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /leaveall - order userbot to leave from all group

⚡ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} **""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
