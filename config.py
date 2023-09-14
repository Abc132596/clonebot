#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6229942949:AAHDJKbZCvJ-CLDCrm59uJ5SADHyniMgtqA")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "21543397"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "87579ffc7be4d3ababdc07cbbc2e8dc4")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFIueUAPpUylNvaEAWw1JNTbSIW3GpYtOpOJVWdZ21G76NgiDT5t8oHDjtPUaH2wkg3FZ39E51W1qvlx8Ejjnw3SN1dqSQjRGyakpUQ0RvFFpm_zk7bbvThGlmYDlrJ4ZgcbOcgCksT61yd7iOEoT_7cN3Z3ClSJFlg3RoW82K04MGo5BKWoTAn0OhP90mXMu7LuFJuAxZ1rqP_s5w4EbonZ6Z90JKh7wFNgSzHx6kdFn7Cs8X7MkuOrK3cE2JNdiPbvGwOEw84p_I57YdRQSQYoCWVYVWu1TZ8q7WSq8LbtN7PIui_3bx8J2AP1vSZN6R-J7uOZzFAv_fEA0_i1s7IkCYvNQAAAAGBtF75AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
