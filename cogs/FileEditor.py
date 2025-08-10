import json, requests
from cogs.Misc import log

class saveConfig():
    def __init__(self, id = None, token = None):
        self.id = id
        self.token = token

    def saveID(self, button):
        try:
            token = loadConfig().loadToken()
            res = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={token}&steamids={self.id}").json()
            if res["response"]["players"] == []:
                button.configure(text="Invalid ID")
                button.after(2500, lambda: button.configure(text="Save ID"))
                return
            with open("data/config.json", "r") as read:
                temp = json.load(read)
                temp["id"] = self.id
            with open("data/config.json", "w") as write:
                json.dump(temp, write, indent=4)
            button.configure(text=f"Saved \"{self.id}\"")
            print(log(False, f"Sucessfully saved \"{self.id}\" into configuration file"))
            button.after(2500, lambda: button.configure(text="Save ID"))
        except Exception as e:
            print(log(True, f"An error occured while saving configuration: {e}"))

    def saveFirst(self):
        try:
            with open("data/config.json", "r") as read:
                temp = json.load(read)
                temp["firstStartup"] = "False"
            with open("data/config.json", "w") as write:
                json.dump(temp, write, indent=4)
            print(log(False, "Updated first startup to \"True\"."))
        except Exception as e:
            print(log(True, f"An error occured while saving configuration: {e}"))

    def saveToken(self, button):
        try:
            res = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.token}&steamid=76561199248652685")
            if res.status_code == 401:
                button.configure(text="Invalid token")
                button.after(2500, lambda: button.configure(text="Save Token"))
                return
            with open("data/config.json", "r") as read:
                temp = json.load(read)
                temp["token"] = self.token
            with open("data/config.json", "w") as write:
                json.dump(temp, write, indent=4)
            print(log(False, f"Updated token to \"{self.token}\"."))
            button.configure(text=f"Saved \"{self.token}\".")
        except Exception as e:
            print(log(True, f"An error occured while saving configuration: {e}"))

class loadConfig():
    def __init__(self):
        pass

    def loadID(self):
        try:
            with open("data/config.json", "r") as read:
                temp = json.load(read)
            return temp["id"]
        except Exception as e:
            print(log(True, f"An error occured while loading configuration: {e}"))

    def loadFirst(self):
        try:
            with open("data/config.json", "r") as read:
                temp = json.load(read)
            return temp["firstStartup"]
        except Exception as e:
            print(log(True, f"An error occured while loading configuration: {e}"))

    def loadToken(self):
        try:
            with open("data/config.json", "r") as read:
                temp = json.load(read)
            return temp["token"]
        except Exception as e:
            print(log(True, f"An error occured while loading configuration: {e}"))
