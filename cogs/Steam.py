import requests, json, os
from cogs.FileEditor import loadConfig
from cogs.Misc import log

def saveAppsAPI():
    games = []
    res = None

    id = loadConfig().loadID()
    if id == None:
        return f"Please set your ID in config."

    try:
        token = loadConfig().loadToken()
        res = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={token}&steamid={id}&format=json&include_appinfo=true")
        print(log(False, f"Successfully fetched all steam games: Code {res.status_code}"))
    except Exception as e:
        print(log(True, f"Error occured in getting steam games : Code {res.status_code} : {e}"))
        return f"Failed to fetch steam games: {e}"

    res = res.json()

    for game in res["response"].get("games", []):
        appid = game["appid"]

        print(log(False, f"Fetching game details for APPID {appid}"))
        try:
            details_res = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appid}").json()
            print(log(False, f"Successfully fetched game details for APPID: {appid} ({game["name"]})"))
            if details_res.get(str(appid), {}).get("success", False):
                details = details_res[str(appid)]["data"]
                games.append(details)
        except Exception as e:
            print(log(True, f"An error occured fetching game details for APPID {appid} ({game["name"]} : {e}"))
            return f"Failed to fetch game details: {e}"

    with open("data/games.json", "w") as f:
        json.dump(games, f, indent=4)

    return f"Saved {len(games)} games."

def loadApps():
    games = []
    with open("data/games.json", "r") as read:
        data = json.load(read)
        for game in data:
            games.append(game)
    return games

def launchApp(appid):
    print(log(False, f"Running appID {appid}"))
    os.system(f'start steam://rungameid/{appid}')