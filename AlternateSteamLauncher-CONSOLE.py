# V1.1
import customtkinter as ctk
from cogs.Misc import log, exceptionthingy
from cogs.ctk.packs import ctkconfig

with open("files/output.txt", "w") as f:
    f.write("")
    log(False, "Initiliazing...")

ctk.CTk.report_callback_exception = exceptionthingy

tk = ctk.CTk()
ctkconfig(tk)
tk.mainloop()