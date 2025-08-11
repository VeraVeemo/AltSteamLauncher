from datetime import datetime
import sys, traceback, requests, zipfile, io, os
import customtkinter as ctk

def download_lol(thing):
    res = requests.get("https://github.com/VeraVeemo/AltSteamLauncher/archive/refs/heads/main.zip")
    print(log(False, "Got new update file"))
    with zipfile.ZipFile(io.BytesIO(res.content)) as zip_ref:
        zip_ref.extractall("../../AltSteamLauncher")
        extracted_folder = os.getcwd() + "/AltSteamLauncher-main"
    print(log(False, "Successfully updated to latest version!"))
    thing.destroy()
    popup = ctk.CTkToplevel()
    popup.title("Message")
    popup.grab_set()
    widget = ctk.CTkTextbox(popup, width=375, height=75)
    widget.insert("0.0", "Successfully updated! The new update is in " + extracted_folder)
    widget.configure(state="disabled", text_color="green")
    widget.pack(padx=10, pady=10, fill="both", expand=True)
    close_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    close_button.pack(pady=(0, 10))
    return extracted_folder

def log(error, msg):
    with open("files/output.txt", "a") as f:
        f.write(f"[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {"[ERROR   ]" if error else "[INFO    ]"} {msg}\n")
    if error:
        return f"\033[31m[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] [ERROR   ] {msg}"
    else:
        return f"\033[92m[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] [INFO    ] {msg}"

def exceptionthingy(self, exc_type, value, tracebacke):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, value, tracebacke)
        return

    error_msg = "".join(traceback.format_exception(exc_type, value, tracebacke))
    print(log(True, error_msg))
    popup = ctk.CTkToplevel()
    popup.title("Error")
    popup.grab_set()

    text_widget = ctk.CTkTextbox(popup, width=600, height=300)
    text_widget.insert("0.0", "Something went wrong!\n\n" + error_msg)
    text_widget.configure(state="disabled", text_color="red")
    text_widget.pack(padx=10, pady=10, fill="both", expand=True)

    close_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    close_button.pack(pady=(0, 10))
    popup.update_idletasks()
    popup.minsize(650, 650)

def updater():
    popup = ctk.CTkToplevel()
    popup.title("Message")
    popup.grab_set()
    widget = ctk.CTkTextbox(popup, width=225, height=75)
    with open(os.getcwd() + "\\AlternateSteamLauncher.pyw", "r") as f:
        e = requests.get("https://api.github.com/repos/VeraVeemo/AltSteamLauncher/releases").json()
        r = f.readlines()[0]
    e = e[0]["tag_name"]
    if not float(e.strip().lstrip("V")) > float(r.strip().lstrip("# V")):
        widget.insert("0.0", "There currently is no update available!")
        widget.configure(state="disabled", text_color="green")
        widget.pack(padx=10, pady=10, fill="both", expand=True)

        close_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        close_button.pack(pady=(0, 10))
    else:
        print(log(False, "New version available: " + e))
        widget.insert("0.0", "There is a new update available!\nUpdate?")
        widget.configure(state="disabled", text_color="green")
        widget.pack(padx=10, pady=10, fill="both", expand=True)

        yuh = ctk.CTkButton(popup, text="Yes", command=lambda: download_lol(popup))
        yuh.pack(pady=(0, 10))

        nah = ctk.CTkButton(popup, text="No", command=popup.destroy)
        nah.pack(pady=(0, 10))
        
def budget_updater():
    # im so lazy
    with open(os.getcwd() + "\\AlternateSteamLauncher.pyw", "r") as f:
        e = requests.get("https://api.github.com/repos/VeraVeemo/AltSteamLauncher/releases").json()
        r = f.readlines()[0]
    e = e[0]["tag_name"]
    if float(e.strip().lstrip("V")) > float(r.strip().lstrip("# V")):
        print(log(False, "New version available: " + e))
        popup = ctk.CTkToplevel()
        popup.title("Message")
        popup.grab_set()
        widget = ctk.CTkTextbox(popup, width=225, height=75)
        widget.insert("0.0", "There is a new update available!\nUpdate?")
        widget.configure(state="disabled", text_color="green")
        widget.pack(padx=10, pady=10, fill="both", expand=True)

        yuh = ctk.CTkButton(popup, text="Yes", command=lambda: download_lol(popup))
        yuh.pack(pady=(0, 10))

        nah = ctk.CTkButton(popup, text="No", command=popup.destroy)
        nah.pack(pady=(0, 10))