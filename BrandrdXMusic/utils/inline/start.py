from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

import config
from BrandrdXMusic import app


# ============================
# 🔹 TEXT FORMAT CHANNEL LIST
# ============================
def channel_list_text():
    return (
        "**📺 CHANNEL LIST**\n\n"
        "MAIN CHANNEL - https://t.me/MAIN_CHANNEL_PR\n"
        "ABOUT PR - https://t.me/+odyFZN1NlkY1OWY9\n"
        "PREMIUM MOD APK - https://t.me/+m7SRWPjJuwA5YTY1\n"
        "PR ALL BOT - https://t.me/+BNhBea8t8RVjODJl\n"
        "EHD - EMPIRE OF HINDI DONGHUA - https://t.me/+HFrcii6ApyJmMDk1\n"
        "PR DUBBER - https://t.me/pr_dubber\n"
        "ROMANCE ANIME - https://t.me/+1DTvXcEKocI3MTZl\n"
        "FINISHED ANIME - https://t.me/+b5UDP-wrby45YmI1\n"
        "ONGOING ANIME (HINDI) - https://t.me/+aIVAn5vVpqU5ZjU9\n"
        "MOVIES & SERIES (HINDI) - https://t.me/+rU-ANw6FaDowNzQ9\n"
        "ALL TYPES SHORTS - https://t.me/All_types_shorts\n"
        "ANIME GIRL PIC - https://t.me/+eT_GB_2-M69jNzQ1\n"
        "🔞 HAREM REALM - https://t.me/HAREM_REALM\n"
        "BACKUP - https://t.me/+PN8TmHPEvG0wOWRl"
    )


# ============================
# 🔹 TEXT FORMAT GROUP LIST
# ============================
def group_list_text():
    return (
        "**💬 GROUP LIST**\n\n"
        "PRIVATE CHATTING GROUP - https://t.me/+CzAjQld8eVM4YjA1\n"
        "MOVIE DISCUSSION GROUP - https://t.me/+TQUksZof7_g1ODRl\n"
        "ANIME DISCUSSION GROUP - https://t.me/+xn-tE5i8_oc3ODJl\n"
        "OWNER - @OWNER_OF_PR"
    )


# ============================
# 🔹 START PANEL (UPDATED)
# ============================
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="📺 CHANNELS", callback_data="show_channels"),
            InlineKeyboardButton(text="💬 GROUPS", callback_data="show_groups"),
        ]
    ]
    return buttons


# ============================
# 🔹 PRIVATE PANEL (UPDATED)
# ============================
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
            InlineKeyboardButton(text="📺 CHANNELS", callback_data="show_channels"),
            InlineKeyboardButton(text="💬 GROUPS", callback_data="show_groups"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons


# ============================
# 🔹 CALLBACK HANDLERS
# ============================

@app.on_callback_query(filters.regex("show_channels"))
async def show_channels(_, query):
    await query.message.edit_text(
        channel_list_text(),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅ BACK", callback_data="settings_back_helper")]]
        )
    )


@app.on_callback_query(filters.regex("show_groups"))
async def show_groups(_, query):
    await query.message.edit_text(
        group_list_text(),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅ BACK", callback_data="settings_back_helper")]]
        )
    )


# ============================
# 🔹 COMMAND HANDLERS
# ============================

@app.on_message(filters.command(["channels", "cl"]))
async def channels_cmd(_, message: Message):
    await message.reply_text(channel_list_text(), disable_web_page_preview=True)


@app.on_message(filters.command(["groups", "gl"]))
async def groups_cmd(_, message: Message):
    await message.reply_text(group_list_text(), disable_web_page_preview=True)