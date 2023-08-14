import math
from datetime import datetime


def generate():
    dt = datetime.today()
    seconds = math.ceil(dt.timestamp())
    mail = f"gamora_zen-whoberi_{seconds}@yandex.ru"
    return mail
