# Copyright (C) 2021 By Arauck

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
        f"""☃️ __Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !__\n
💭 **{BOT_NAME}** __{will help to play music & video on the video chat of telegram!__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("ʙᴀsɪᴄ ᴄᴍᴅ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbcmds"),
                ],
                [
                    InlineKeyboardButton(
                        "ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Aruacksupport"
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
        f"""❓ __Basic ᴄᴍᴅ for using this bot:__

1.) __First, add me to your group.__
2.) __Then, promote me as administrator and give all permissions except Anonymous Admin.__
3.) __After promoting me, type /reload in group to refresh the admin data.__
3.) __Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.__
4.) __Turn on the video chat first before start to play video/music.__
5.) __Sometimes, reloading the bot by using /reload command can help you to fix some problem.__

📌 __If the userbot havent joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.__

💡 __If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}__

⚡ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} ** """,
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
        f"""🏮 __Here is the basic commands:__

» **/play** (song name/link) - __play music on video chat__
» **/stream** (query/link) - __stream the yt live/radio live music__
» **/vplay** (video name/link) - __play video on video chat__
» **/vstream** - __play live video from yt live__
» **/playlist** - __show you the playlist__
» **/video** (query) - __download video from youtube__
» **/song** (query) - __download song from youtube__
» **/lyric** (query) - __scrap the song lyric__
» **/search** (query) - __search a youtube video link__

» **/ping** - __show the bot ping status__
» **/uptime** - __show the bot uptime status__
» **/alive** - __show the bot alive info (in group)__

⚡️ **ᴾᴼᵂᴱᴿᴱᴰ ᴮʸ {BOT_NAME} **""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» **/pause** - __pause the stream__
» **/resume** - __resume the stream__
» **/skip** - __switch to next stream__
» **/stop** - __stop the streaming__
» **/vmute** - __mute the userbot on voice chat__
» **/vunmute** - __unmute the userbot on voice chat__
» **/reload** - __reload bot and refresh the admin data__
» **/userbotjoin** - i__nvite the userbot to join group__
» **/userbotleave** - __order userbot to leave from group__

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

