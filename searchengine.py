# create a google search engine using GUI
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def on_closing():  # close the window and exit from python
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
def search():
    webbrowser.open('https://www.google.com/search?q=' + entry.get())
root = Tk()
root.title('Google')
root.geometry('300x100')
root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", on_closing)
label = ttk.Label(root, text='Enter text to search:')
label.pack()
entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text='Search', command=search)
button.pack()
root.mainloop()