import requests
import customtkinter as ctk
from PIL import Image
from io import BytesIO
from cogs.Steam import loadApps, launchApp, saveAppsAPI
from cogs.Misc import log
from cogs.FileEditor import loadConfig
num = 0

def reloadApps(button, scroll):
    print(log(False, "Destroying all current games"))
    for widget in scroll.winfo_children():
        print(log(False, f"Destroyed {widget}"))
        widget.destroy()

    games = loadApps()
    for i, game in enumerate(games):
        print(log(False, f"Fetching game details for game {game["name"]}..."))
        name = game.get("name", "Unknown Game")
        appid = game.get("steam_appid")
        header = game.get("header_image", None)
        desc = game.get("short_description", "No description available.")
        if len(desc) > 125:
            desc = desc[:125] + "..."
        card = ctk.CTkFrame(scroll)
        card.grid(row=i, column=0, padx=10, pady=10, sticky="ew")
        card.grid_columnconfigure(1, weight=1)

        if header:
            try:
                print(log(False, f"Getting image for the game"))
                img_data = requests.get(header).content
                pil_img = Image.open(BytesIO(img_data)).resize((200, 100))
                img_ctk = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(200, 100))
                img_label = ctk.CTkLabel(card, image=img_ctk, text="")
                img_label.grid(row=0, column=0, rowspan=3, padx=10, pady=5)
                print(log(False, f"Got image!"))
            except Exception as e:
                print(log(True, f"Error occured in fetching image: {e}"))
                pass

        print(log(False, f"Setting up card for the game..."))
        name_label = ctk.CTkLabel(card, text=name, font=ctk.CTkFont(size=16, weight="bold"))
        name_label.grid(row=0, column=1, sticky="w", pady=(5, 0))
        desc_label = ctk.CTkLabel(card, text=desc, wraplength=400, justify="left")
        desc_label.grid(row=1, column=1, sticky="w")
        launch_btn = ctk.CTkButton(card, text="Launch Game", command=lambda a=appid: launchApp(a))
        launch_btn.grid(row=2, column=1, sticky="w", pady=(5, 5))
        print(log(False, f"Set up card for the game!"))

    print(log(False, f"Loaded all games and cards!"))
    button.configure(text="Loaded all games!")
    button.after(2500, lambda: button.configure(text="Load Games"))

def saveApps(button, sigma, scroll):
    msg = saveAppsAPI()
    button.configure(text=msg)
    reloadApps(sigma, scroll)
    button.after(2500, lambda: button.configure(text="Save Games"))

def unloadApps(button, scroll):
    for widget in scroll.winfo_children():
        widget.destroy()

    print(log(False, f"Unloaded all games"))
    button.configure(text="Unloaded all games")
    button.after(2500, lambda: button.configure(text="Unload Games"))

def clicker(button):
    global num
    num += 1
    print(log(False, f"Updated clicker number to {num}"))
    button.configure(text=f"Clicker: {num}")

def resetclicks(button, reset):
    global num
    num = 0
    print(log(False, f"Reset clicker number to {num}"))
    button.configure(text="Clicker")
    reset.configure(text=f"Clicks reset!")
    reset.after(2500, lambda: reset.configure(text="Reset"))

def refreshInfo(text, button):
    print(log(False, f"Refreshed info text!"))
    text.configure(text=f"Version: 1.1\nGitHub Repo: AltSteamLauncher\nToken: {loadConfig().loadToken()}\nSteamID: {loadConfig().loadID()}\nFirst Launch: {loadConfig().loadFirst()}")
    button.configure(text="Refreshed info!")
    button.after(2500, lambda: button.configure(text="Refresh"))