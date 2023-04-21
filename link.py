import pyshorteners
from tkinter import *

ms = Tk ()
ms.geometry("400x250")
ms.configure(bg="purple")
#button function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    
    entry2.insert(END,s)
# label for enter user url
Label(ms, text="Enter Your Url Link", font="impack 15 bold", bg="black", fg="white").pack(fill = "x")
# entry box
entry1= Entry(ms, font="10", bd=2, width=30)
entry1.pack(pady=30)
#button
Button(ms, text="click" , font="impack 12 bold", bg="black", fg="white", width="10",command=short).pack()
#entry
entry2 = Entry(ms, font="impack 15 bold", bg="purple",bd=0, width=25,)
entry2.pack(pady= 30)
mainloop()