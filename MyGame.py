from tkinter import *
from tkinter import messagebox as msb

window = Tk()

window.title('Are you sure?')
window.geometry('350x200')
oldman = PhotoImage(file='sprite-pixel-art-maker-error-sans-pixel-art-11563482698igeq5r09mw.png')
window.iconphoto(False, oldman)

def pudelko():
    msb.showinfo("Error", "You have been hijacked by Meloshke :)")

baton = Button(window, text='Are you sure you want to open this file?', bd = '1', command =lambda: pudelko())

baton.pack(side = 'top')
window.mainloop()