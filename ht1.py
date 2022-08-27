from cProfile import label
from cgitb import text
from re import A
import tkinter as tk
from typing import Sized
from requests import delete
import tkinter.font as font

def additem():
    listbox.insert(tk.END, content.get())
    entery.delete(0,tk.END)

def deletelist():
    listbox.delete(0, tk.END)

def deleteitemselected():
    listbox.delete(tk.ANCHOR)

window = tk.Tk()
window.title('Tkinter Project')

label = tk.Label(window, text="Students List", padx=10, pady=10,  font=("Arial", 55)).pack()

add_font = font.Font(family='Helvetica', size=16, weight='bold')
add_button = tk.Button(window,text="Add Elements",font=add_font, command=additem, bg="grey", fg = 'white',padx=10, pady=10,)
add_button.pack()

delete_font = font.Font(family='Helvetica', size=16, weight='bold')
delete_button = tk.Button(window, text="Delete List",font=delete_font, command=deletelist, bg="grey",fg = 'white', padx=10, pady=10)
delete_button.pack()

delete_selected_font = font.Font(family='Helvetica', size=16, weight='bold')
delete_selected_button = tk.Button(window, text="Delete selected Item", font=delete_selected_font, bg="grey", fg = 'white', padx=10, pady=10,  command=deleteitemselected)
delete_selected_button.pack()

content = tk.StringVar()
entery = tk.Entry(window, width=45,font=('Arial 24'), textvariable=content)
entery.pack()

# box_font = font.Font(size=15)
window.geometry("750x250")
listbox = tk.Listbox(window, width=100, height=30,fg = 'green')
listbox.pack()

window.mainloop()

