import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

def motion(event):
    x_motion = (window.winfo_pointerx() - window.winfo_rootx()) / window.winfo_width()
    y_motion = 1 - (window.winfo_pointery() - window.winfo_rooty()) / window.winfo_height()
    x.set(x_motion)
    y.set(y_motion)
    print('{}, {}'.format(x_motion, y_motion))

# Window
# window = Tk()
window = ThemedTk(theme="scidblue")
[width,height]=[475,400]
window.geometry(f'{width}x{height}')
window.title('Servo Controller')

bg = PhotoImage(file=sys.path[0]+"\img\space.png")
my_label = Label(window, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# -----------Yaw Bar------------
yaw_frame = ttk.Frame(window, width=350, height=75, borderwidth=5, relief = tk.GROOVE)
yaw_frame.pack_propagate(False)
yaw_frame.pack(
    side = 'left',
    padx = 15
    )

x = IntVar()
yaw_label = Label(yaw_frame, text ='Yaw', font="24")
yaw_label.pack()

yaw_bar = ttk.Progressbar(
    yaw_frame, 
    orient=HORIZONTAL, 
    length=300, 
    mode="determinate", max=1
    )
yaw_bar.pack()
yaw_bar.start()
yaw_bar.stop()
yaw_bar.config(variable=x)

#------------Pitch Bar-------------
pitch_frame = ttk.Frame(window, width=100, height=300, borderwidth=5, relief = tk.GROOVE)
pitch_frame.pack_propagate(False)
pitch_frame.pack(
    side = 'right',
    padx = 15
    )

y = IntVar()
pitch_label = Label(pitch_frame, text ='Pitch', font="24")
pitch_label.pack(side = 'top')

pitch_bar = ttk.Progressbar(
    pitch_frame, 
    orient=VERTICAL, 
    length=300, 
    mode="determinate", max=1
    )
pitch_bar.pack()
pitch_bar.start()
pitch_bar.stop()
pitch_bar.config(variable=y)


window.bind('<Motion>', motion)
window.mainloop()