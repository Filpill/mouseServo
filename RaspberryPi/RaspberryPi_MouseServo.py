# import tkinter as tk
# from tkinter import ttk
# from numpy import interp

# # Window
# window = tk.Tk()
# window.title('Sliders')

# # Slider
# scale_int = tk.IntVar(value=128)
# scale = ttk.Scale(
#     window, 
#     command=lambda value: print(scale_int.get()),
#     from_=0,
#     to=255,
#     length=300,
#     orient = 'horizontal',
#     variable = scale_int
#       )
# scale.pack()

# # Progress Bar
# progress = ttk.Progressbar(
#     window,
#     variable = scale_int,
#     orient = 'horizontal',
#     mode = 'indeterminate',
#     length = 400
#     )
# progress.pack()

# # Run
# window.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import ttk

def motion(event):
    yaw_proportion = event.x / event.widget.winfo_width()
    pitch_proportion = event.y / -event.widget.winfo_height()
    yaw_value.set(yaw_proportion)
    pitch_value.set(pitch_proportion)

# Window
window = tk.Tk()
window.geometry('450x400')
window.title('Frames and parenting')

# -----------Yaw Bar------------
yaw_frame = ttk.Frame(window, width=350, height=100, borderwidth=10, relief = tk.GROOVE)
yaw_frame.pack_propagate(False)
yaw_frame.pack(side = 'left')

yaw_value = IntVar()
yaw_label = Label(yaw_frame, text ='Yaw', font="50")
yaw_label.pack(pady=1)

yaw_bar = ttk.Progressbar(
    yaw_frame, 
    orient=HORIZONTAL, 
    length=300, 
    mode="determinate", max=1)
yaw_bar.pack(side = 'left')
yaw_bar.start()
yaw_bar.stop()
yaw_bar.bind('<B1-Motion>', motion)
yaw_bar.config(variable=yaw_value)

#------------Pitch Bar-------------
pitch_frame = ttk.Frame(window, width=75, height=300, borderwidth=10, relief = tk.GROOVE)
pitch_frame.pack_propagate(False)
pitch_frame.pack(side = 'right')

pitch_value = IntVar()
pitch_label = Label(pitch_frame, text ='Pitch', font="50")
pitch_label.pack(side = 'top')

pitch_bar = ttk.Progressbar(
    pitch_frame, 
    orient=VERTICAL, 
    length=300, 
    mode="determinate", max=1)
pitch_bar.pack()
pitch_bar.start()
pitch_bar.stop()
pitch_bar.bind('<B1-Motion>', motion)
pitch_bar.config(variable=pitch_value)

window.mainloop()