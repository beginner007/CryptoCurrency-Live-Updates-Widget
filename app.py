from tkinter import *
import requests
import json
import sched, time
from constants import HOST, UPDATE_FREQUENCY

def updateData(frame=None):

    data = requests.get(HOST)
    print("Updating data...")
    data = data.json()
    label = Label(frame, text=data['BTC']['last_traded_price'])
    label.place(x=140, y=30)
    label = Label(frame, text=data['XRP']['last_traded_price'])
    label.place(x=140, y=55)
    label = Label(frame, text=data['NEO']['last_traded_price'])
    label.place(x=143, y=80)
    label = Label(frame, text=data['GAS']['last_traded_price'])
    label.place(x=140, y=105)
    label = Label(frame, text=data['ETH']['last_traded_price'])
    label.place(x=140, y=130)
    label = Label(frame, text=data['XLM']['last_traded_price'])
    label.place(x=140, y=155)
    root.after(UPDATE_FREQUENCY, updateData)

root = Tk()

w = 300
h = 200
x = 1145
y = 530

# Setting height
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# Prevent resizing
root.resizable(width=False, height=False)
# Window title
root.title('Crypto Live Feed!')
frame = Frame(root, bg='lightblue')
frame.pack(fill='both', expand=True)
# Window color
root.config(background="lightblue")
# # Transparent Window
# root.wait_visibility(root)
# root.wm_attributes('-alpha',0.1)
# Fetch Data
label = Label(frame, text="BTC (INR)   : ")
label.place(x=70, y=30)
label = Label(frame, text="XRP (INR)   : ")
label.place(x=70, y=55)
label = Label(frame, text="NEO (INR)   : ")
label.place(x=70, y=80)
label = Label(frame, text="GAS (INR)   : ")
label.place(x=70, y=105)
label = Label(frame, text="ETH (INR)   : ")
label.place(x=70, y=130)
label = Label(frame, text="XLM (INR)   : ")
label.place(x=70, y=155)
starttime=time.time()

root.after(3000, updateData)
root.mainloop()
