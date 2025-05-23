import datetime
import os

def handle_merge():
    t = datetime.datetime.now().strftime("%d.%m.%y %H.%M.%S")
    p = os.path.join("Filters", t)
    os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "merged.xlsx"), "w").close()
    return p
