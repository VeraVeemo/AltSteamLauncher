import customtkinter as ctk
from cogs.Misc import log
from cogs.ctk.packs import ctkconfig

with open("output.txt", "w") as f:
    f.write("")
    log(False, "Initiliazing...")

tk = ctk.CTk()
ctkconfig(tk)
tk.mainloop()