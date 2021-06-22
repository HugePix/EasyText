import webbrowser

import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

FILE_NAME = tkinter.NONE

def new_file():
	global FILE_NAME
	FILE_NAME = "Unnamed"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Saving file error")

def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def info():
	messagebox.showinfo("About EasyText", "HugePix\nVersion: 1.1 Beta\n[EN]\nBeta")


def updates():
	webbrowser.open("https://sites.google.com/view/easytextbeta/")

def FAQ():
	webbrowser.open("https://sites.google.com/view/easytextbeta/faq/")

def about_beta():
	messagebox.showinfo("What is beta?", "Beta versions are made to test apps/games/website\nThese versions may contain errors\nCurrect version: 1.1 Beta")

def error_report():
	webbrowser.open("https://sites.google.com/view/easytextbeta/report/")
	messagebox.showinfo("Thank you!", "We are sorry, we will try to fix everything soon\nPlease check for updates, you may use and old version\nCurrect version: 1.1 Beta")

def github():
	messagebox.showerror("Error", "Sorry, but now EasyText is not avaible on GitHub, it will be avaible in version 1.2\nCurrect version: 1.1 Beta\nYou may try to check for updates")

root = tkinter.Tk()
root.title("HugePix EasyText Beta 1.1")

root.minsize(width=500, height=500)
root.maxsize(width=2000, height=2000)

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
file = tkinter.Menu(menuBar)
file.add_command(label="New", command = new_file)
file.add_command(label="Open", command = open_file)
file.add_command(label="Save", command = save_file)
file.add_command(label="Save as", command = save_as)

help = tkinter.Menu(menuBar)
help.add_command(label="Website", command = updates)
help.add_command(label="FAQ", command = FAQ)
help.add_command(label="What is beta?", command = about_beta)
help.add_command(label="Report an error", command = error_report)

exit = tkinter.Menu(menuBar)
exit.add_command(label="quit", command = root.quit())

info = tkinter.Menu(menuBar)
info.add_command(label="About EasyText", command = info)
info.add_command(label="EasyText on GitHub", command = github)

updatescentre = tkinter.Menu(menuBar)
updatescentre.add_command(label="check for updates", command = updates)

menuBar.add_cascade(label="File", menu=file)
menuBar.add_cascade(label="quit", menu=exit)
menuBar.add_cascade(label="updates...", menu = updatescentre)
menuBar.add_cascade(label="Help", menu=help)
root.config(menu=menuBar)
root.mainloop()