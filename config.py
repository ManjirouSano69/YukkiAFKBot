#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "22867431"))
API_HASH = getenv("API_HASH", "24ef0e76ceb137563dc33722e4cd79bd")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7483130894:AAH9VSFstcInQmPS2NGEKv5ivcq_XtAfkx8")

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://niksharma92297:afk@cluster0.wj4ftow.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "1993048420 5743248220 5150045729 1214348787 6297086120").split())
)  # Input type must be interger
