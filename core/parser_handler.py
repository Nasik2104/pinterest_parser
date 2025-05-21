import datetime
import os

def handle_parse(q):
    t = datetime.datetime.now().strftime("%d.%m.%y %H.%M.%S")
    p = os.path.join("Search", t)
    os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "result.xlsx"), "w").close()
    return p
