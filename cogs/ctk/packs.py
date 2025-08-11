from PIL import ImageDraw
from customtkinter import CTkFont
from cogs.ctk.callbacks import *
from cogs.Misc import updater, budget_updater
from cogs.FileEditor import loadConfig, saveConfig
from io import BytesIO

def ctkconfig(tk):
    temp = loadConfig()
    temp2 = saveConfig()
    data = loadConfig.loadFirst(temp)
    print(log(False, f"Setting up configuration for UI"))
    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("system")
    tk.iconbitmap("files/appicon.ico")
    tk.resizable(False, False)
    tk.grid_rowconfigure(1, weight=1)
    tk.grid_columnconfigure(0, weight=1)
    tk.title("Alternate Steam Launcher")
    tk.geometry("800x600")
    print(log(False, f"Configuration complete"))

    print(log(False, f"Creating tabview"))
    tabview = ctk.CTkTabview(tk, 780, 590)
    tabview.grid()
    tabview.add("Games")
    tabview.add("Config")
    tabview.add("Info")
    if data == "True":
        tabview.set("Config")
        saveConfig.saveFirst(temp2)
    print(log(False, f"Tabview created"))

    print(log(False, f"Setting up buttons for tabview \"Games\""))
    top = ctk.CTkFrame(master=tabview.tab("Games"))
    top.grid(row=0, column=0, sticky="ew")

    scroll = ctk.CTkScrollableFrame(master=tabview.tab("Games"), width=760, height=500)
    scroll.grid(row=1, column=0, sticky="nsew")

    refresh = ctk.CTkButton(top, text="Load Games", command=lambda: reloadApps(refresh, scroll))
    refresh.pack(padx=8, pady=5, side="left")

    unload = ctk.CTkButton(top, text="Unload Games", command=lambda: unloadApps(unload, scroll))
    unload.pack(padx=8, pady=5, side="left")

    load = ctk.CTkButton(top, text="Save Games", command=lambda: saveApps(load, refresh, scroll))
    load.pack(padx=8, pady=5, side="left")

    eat = ctk.CTkButton(top, text="Clicker", command=lambda: clicker(eat))
    eat.pack(padx=8, pady=5, side="left")

    reset = ctk.CTkButton(top, text="Reset", command=lambda: resetclicks(eat, reset))
    reset.pack(padx=8, pady=5, side="left")
    print(log(False, f"Set up buttons for tabview \"Games\"!"))

    print(log(False, f"Setting up buttons for tabview \"Config\""))
    top2 = ctk.CTkFrame(master=tabview.tab("Config"))
    top2.pack(anchor="center")

    IDentry = ctk.CTkEntry(top2, placeholder_text="Enter your steam ID")
    IDentry.pack(padx=12, pady=6)

    IDbutton = ctk.CTkButton(top2, text="Save ID", command=lambda: saveConfig(IDentry.get()).saveID(IDbutton))
    IDbutton.pack(padx=8, pady=5)

    Tokenentry = ctk.CTkEntry(top2, placeholder_text="Enter your API Token")
    Tokenentry.pack(padx=12, pady=6)

    Tokenbutton = ctk.CTkButton(top2, text="Save Token", command=lambda: saveConfig(Tokenentry.get()).saveToken(Tokenbutton))
    Tokenbutton.pack(padx=8, pady=5)
    print(log(False, f"Set up buttons for tabview \"Config\"!"))

    print(log(False, f"Setting up UI for tabview \"Info\""))
    top3 = ctk.CTkFrame(master=tabview.tab("Info"))
    top3.pack(anchor="center")

    devtext = ctk.CTkLabel(top3, text="Developers", text_color="red", font=CTkFont("Arial", 24, "bold",  underline=True), anchor="center")
    devtext.grid(row=0, column=0, padx=6, pady=14, sticky="nsew", columnspan=2)

    temp3 = requests.get("https://api.lanyard.rest/v1/users/333585549837336577").json()
    res = requests.get(f"https://cdn.discordapp.com/avatars/333585549837336577/{temp3["data"]["discord_user"]["avatar"]}")
    img = Image.open(BytesIO(res.content)).convert("RGBA")
    img = img.resize((75, 75), Image.LANCZOS)
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
    img.putalpha(mask)
    aveemo = ctk.CTkImage(img, size=(75, 75))
    avlabel = ctk.CTkLabel(top3, image=aveemo, text="")
    avlabel.grid(row=1, column=0, padx=8, pady=5)

    avtext = ctk.CTkLabel(top3, text="AVeemo\nMain Developer", text_color="#0bda51", font=CTkFont("Arial", 16, "bold"))
    avtext.grid(row=1, column=1, padx=6, pady=6)

    helperstext = ctk.CTkLabel(top3, text="Helpers", text_color="yellow", font=CTkFont("Arial", 24, "bold", underline=True), anchor="center")
    helperstext.grid(row=2, column=0, padx=6, pady=14, sticky="nsew", columnspan=2)

    res = requests.get(f"https://veraveemo.uk/Files/uni.png")
    img = Image.open(BytesIO(res.content)).convert("RGBA")
    img = img.resize((75, 75), Image.LANCZOS)
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
    img.putalpha(mask)
    uni = ctk.CTkImage(img, size=(75, 75))
    unilabel = ctk.CTkLabel(top3, image=uni, text="")
    unilabel.grid(row=3, column=0, padx=8, pady=5)

    unitext = ctk.CTkLabel(top3, text="Macchiato\nIdea Guy", text_color="gray", font=CTkFont("Arial", 16, "bold"), anchor="center")
    unitext.grid(row=3, column=1, padx=6, pady=6, sticky="nsew")

    extratext = ctk.CTkLabel(top3, text="Extra", text_color="dark green", font=CTkFont("Arial", 24, "bold", underline=True), anchor="s")
    extratext.grid(row=4, column=0, padx=6, pady=14, sticky="s", columnspan=2)

    text = ctk.CTkLabel(top3, text=f"Version: 1.1\nGitHub Repo: AltSteamLauncher\nToken: {loadConfig().loadToken()}\nSteamID: {loadConfig().loadID()}\nFirst Launch: {loadConfig().loadFirst()}", font=CTkFont("Arial", 12), anchor="s")
    text.grid(row=5, column=0, padx=6, pady=6, sticky="s", columnspan=2)

    textrefresh = ctk.CTkButton(top3, 2, 2, text="Refresh", command=lambda: refreshInfo(text, textrefresh))
    textrefresh.grid(row=6, column=0, padx=6, pady=6, columnspan=2)

    update = ctk.CTkButton(top3, 4, 4, text="Check for Updates", command=updater)
    update.grid(row=7, column=0, padx=6, pady=6, columnspan=2)

    print(log(False, f"Set up UI for tabview \"Info\"!"))

    print(log(False, "Initiliazing UI..."))
    reloadApps(refresh, scroll)
    print(log(False, "UI Initialized!"))
    budget_updater()