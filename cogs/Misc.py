from datetime import datetime

def log(error, msg):
    with open("output.txt", "a") as f:
        f.write(f"[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {"[ERROR   ]" if error else "[INFO    ]"} {msg}\n")
    if error:
        return f"\033[31m[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] [ERROR   ] {msg}"
    else:
        return f"\033[92m[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] [INFO    ] {msg}"