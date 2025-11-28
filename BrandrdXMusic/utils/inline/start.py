from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from BrandrdXMusic import app  # your main Client instance

# ======================================
#           START PANEL BUTTONS
# ======================================

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ]
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="📜 GROUPS", callback_data="show_groups"),
            InlineKeyboardButton(text="📺 CHANNELS", callback_data="show_channels"),
        ],
        [InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID)],
    ]
    return buttons

# ======================================
#           CHANNELS & GROUPS HTML
# ======================================

CHANNELS_TXT = """
<b>📢 ᴏꜰꜰɪᴄɪᴀʟ ᴘʀ ᴄʜᴀɴɴᴇʟꜱ</b>

<b>›› ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ:</b> <a href='https://t.me/MAIN_CHANNEL_PR'>ᴍᴀɪɴ ᴘʀ ᴄʜᴀɴɴᴇʟ</a>

<blockquote expandable>
<b>›› ᴀʙᴏᴜᴛ ᴘʀ:</b> <a href='https://t.me/+odyFZN1NlkY1OWY9'>ᴀʙᴏᴜᴛ ᴘʀ</a>
<b>›› ᴘʀᴇᴍɪᴜᴍ ᴍᴏᴅ ᴀᴘᴋ:</b> <a href='https://t.me/+m7SRWPjJuwA5YTY1'>ᴘʀᴇᴍɪᴜᴍ ᴍᴏᴅ ᴀᴘᴋ</a>
<b>›› ᴘʀ ᴀʟʟ ʙᴏᴛ:</b> <a href='https://t.me/+BNhBea8t8RVjODJl'>ᴘʀ ᴀʟʟ ʙᴏᴛ</a>
<b>›› ᴇʜᴅ – ᴇᴍᴘɪʀᴇ ᴏꜰ ʜɪɴᴅɪ ᴅᴏɴɢʜᴜᴀ:</b> <a href='https://t.me/+HFrcii6ApyJmMDk1'>ᴇʜᴅ – ᴅᴏɴɢʜᴜᴀ</a>
<b>›› ᴘʀ ᴅᴜʙʙᴇʀ:</b> <a href='https://t.me/pr_dubber'>ᴘʀ ᴅᴜʙʙᴇʀ</a>
<b>›› ʀᴏᴍᴀɴᴄᴇ ᴀɴɪᴍᴇ:</b> <a href='https://t.me/+1DTvXcEKocI3MTZl'>ʀᴏᴍᴀɴᴄᴇ ᴀɴɪᴍᴇ</a>
<b>›› ꜰɪɴɪꜱʜᴇᴅ ᴀɴɪᴍᴇ:</b> <a href='https://t.me/+b5UDP-wrby45YmI1'>ꜰɪɴɪꜱʜᴇᴅ ᴀɴɪᴍᴇ</a>
<b>›› ᴀʟʟ ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ɪɴ ʜɪɴᴅɪ:</b> <a href='https://t.me/+aIVAn5vVpqU5ZjU9'>ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ</a>
<b>›› ᴀʟʟ ᴏɴɢᴏɪɴɢ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs:</b> <a href='https://t.me/+rU-ANw6FaDowNzQ9'>ᴍᴏᴠɪᴇs & sᴇʀɪᴇs</a>
<b>›› ᴀʟʟ ᴛʏᴘᴇs sʜᴏʀᴛs:</b> <a href='https://t.me/All_types_shorts'>ᴏɴʟʏ sʜᴏʀᴛs</a>
<b>›› ᴀɴɪᴍᴇ ɢɪʀʟ ᴘɪᴄ:</b> <a href='https://t.me/+eT_GB_2-M69jNzQ1'>ᴘɪᴄ</a>
<b>›› ʙᴀᴄᴋᴜᴘ:</b> <a href='https://t.me/+PN8TmHPEvG0wOWRl'>ʙᴀᴄᴋᴜᴘ</a>
<b>›› ʜᴀʀʟᴇᴍ ʀᴇᴀʟᴍ:</b> <a href='https://t.me/+7FwL6dmXhtIwMzFl'>ʜᴀʀʟᴇᴍ ʀᴇᴀʟᴍ</a>
<b>›› ᴅᴇᴠᴇʟᴏᴘᴇʀ:</b> @OWNER_OF_PR
</blockquote>
"""

GROUPS_TXT = """
<b>💬 ᴏꜰꜰɪᴄɪᴀʟ ᴘʀ ɢʀᴏᴜᴘꜱ</b>

<b>›› ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘ:</b>
<a href='https://t.me/+CzAjQld8eVM4YjA1'>ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ</a>

<blockquote expandable>
<b>›› ᴍᴏᴠɪᴇ ᴅɪsᴄᴜssɪᴏɴ ɢʀᴏᴜᴘ:</b>
<a href='https://t.me/+TQUksZof7_g1ODRl'>ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ</a>
<b>›› ᴀɴɪᴍᴇ ᴅɪsᴄᴜssɪᴏɴ ɢʀᴏᴜᴘ:</b>
<a href='https://t.me/+xn-tE5i8_oc3ODJl'>ᴀɴɪᴍᴇ ɢʀᴏᴜᴘ</a>
<b>›› ᴏᴡɴᴇʀ:</b> @OWNER_OF_PR
<b>›› ɢʀᴏᴜᴘ:</b> <a href='https://t.me/pr_dubber_chat'>ɢʀᴏᴜᴘ</a>
</blockquote>
"""

# ======================================
# CALLBACK QUERIES FOR BUTTONS
# ======================================

@app.on_callback_query(filters.regex("show_channels"))
async def callback_show_channels(_, query):
    await query.answer()
    await query.message.edit(
        CHANNELS_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅ BACK", callback_data="settings_back_helper")]]
        )
    )

@app.on_callback_query(filters.regex("show_groups"))
async def callback_show_groups(_, query):
    await query.answer()
    await query.message.edit(
        GROUPS_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅ BACK", callback_data="settings_back_helper")]]
        )
    )

# ======================================
# COMMANDS: /channels & /groups
# ======================================

@app.on_message(filters.command("channels"))
async def cmd_channels(_, message: Message):
    await message.reply(
        CHANNELS_TXT,
        disable_web_page_preview=True,
        quote=True,
    )

@app.on_message(filters.command("groups"))
async def cmd_groups(_, message: Message):
    await message.reply(
        GROUPS_TXT,
        disable_web_page_preview=True,
        quote=True,
    )