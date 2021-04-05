from tkinter import *
from v1 import proceed_arguments
from Tools import getListFromFile

data = getListFromFile()

def search():
    try:
        area.config(text=proceed_arguments(request.get(), data))
    except Exception as err:
        area.config(text=err)

root = Tk()
root.title('Covid')
root.geometry('700x800')
font = ('Arial', 16)
frame = Frame(root)
frame.pack(pady=20)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
request = StringVar(root)
input_tk = Entry(frame, textvariable=request, font=font, width=35)
input_tk.pack(side=LEFT, fill='x')
btn = Button(frame, text='Search', command=search, font=font)
btn.pack(side=LEFT)
area = Label(text='Nothing to show', font=('Arial', 13), justify=LEFT)
area.pack(fill=Y, expand=1)
root.mainloop()

if __name__ == '__main__':
    search()
