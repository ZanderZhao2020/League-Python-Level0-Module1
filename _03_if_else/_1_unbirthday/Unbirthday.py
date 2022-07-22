from tkinter import simpledialog, messagebox
Date = simpledialog.askstring("Prompt", "Enter your birthday (mm/dd)")
if Date == "07/22":
	messagebox.showinfo("Message", "Happy birthday")
else:
	messagebox.showinfo("Message", "Happy unbirthday")