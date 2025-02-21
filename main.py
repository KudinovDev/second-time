from tkinter import *
import time 
from datetime import datetime

temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = window.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label_second.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget()
    btnStop.pack(pady=10)
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack(pady=10)
    btnReset.pack()
    window.after_cancel(after_id)

def continue_tick():
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def reset_tick():
    global temp
    temp = 0
    label_second.configure(text='00:00')
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack(pady=10)


window = Tk()
window.geometry('400x600')
window.resizable(width = False, height = False) 
window.title('second time')
window.config(bg = '#464543')

time_label = Label(window, font = ("Comic Sans MS", 40), fg = 'white', bg = '#464543')
time_label.pack(pady=70)

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    window.after(1000, update_time)
update_time()

label_second = Label(window, width=10, font=('Comic Sans MS', 30), text='00:00', fg='white', bg='#464543')
label_second.pack()

btnStart = Button(window, text = 'Старт',
    font = ("Comic Sans MS", 13),
    width = '7',
    height = '3',
    bg = '#AC6700',
    activebackground = '#6D4200',
    activeforeground = 'white',
    command=start_tick
    )

btnStop = Button(window, text = 'Стоп',
    font = ("Comic Sans MS", 13),
    width = '7',
    height = '3',
    bg = '#AC6700',
    activebackground = '#6D4200',
    activeforeground = 'white',
    command=stop_tick
    )

btnContinue = Button(window, text = 'Продолж.',
    font = ("Comic Sans MS", 13),
    width = '8',
    height = '3',
    bg = '#AC6700',
    activebackground = '#6D4200',
    activeforeground = 'white',
    command=continue_tick
    )

btnReset = Button(window, text = 'Сброс',
    font = ("Comic Sans MS", 13),
    width = '7',
    height = '3',
    bg = '#AC6700',
    activebackground = '#6D4200',
    activeforeground = 'white',
    command=reset_tick
    )

btnStart.pack(pady=10)

window.mainloop()

