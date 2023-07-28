import sys
import time
import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from gpiozero import AngularServo


def setup(pin,frequency):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
    pwm=GPIO.PWM(pin,frequency)
    pwm.start(0)
    return pwm

# Setting up Program
GPIO.setmode(GPIO.BCM)
frequency=50
yaw_pwm = setup(23,frequency)
pitch_pwm = setup(24,frequency)
pwm_list = [yaw_pwm,pitch_pwm]

def motion(event,pwm_list):
    
    # Calculate Position of Mouse Pointer On Screen Based on Screen Resolution
    x_motion = (window.winfo_pointerx() - window.winfo_rootx()) / window.winfo_width()
    y_motion = 1 - (window.winfo_pointery() - window.winfo_rooty()) / window.winfo_height()
    
    #Convert to Servo Angle
    x_angle = int(x_motion * 180)
    y_angle = int(y_motion * 180)
    yaw_label.config(text='Yaw: '+'{:02d}'.format(x_angle))
    pitch_label.config(text='Pitch: '+'{:02d}'.format(y_angle))
    
    # Set data for the progress bar
    x.set(x_motion)
    y.set(y_motion)

    # Change Duty Cycle of Servos
    print("x",x_angle,"y",y_angle)
    for i,pwm in enumerate(pwm_list):
        if i == 0:
            servo_angle = x_angle
        else:
            servo_angle = y_angle
        pwm.ChangeDutyCycle(1/18*servo_angle + 2)
    #time.sleep(0.1)

# Window
window = ThemedTk(theme="scidblue")
[width,height]=[575,500]
window.geometry(f'{width}x{height}')
window.title('Servo Controller')

bg_file = "space.png"
if 'win' in sys.platform:
    bg_path = sys.path[0]+fr"\img\{bg_file}"
else:
    bg_path = sys.path[0]+fr"/img/{bg_file}"
bg = PhotoImage(file=bg_path)
my_label = Label(window, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# -----------Yaw Bar------------
yaw_frame = ttk.Frame(window, width=350, height=75, borderwidth=5, relief = tk.GROOVE)
yaw_frame.pack_propagate(False)
yaw_frame.pack(
    side = 'left',
    padx = 25
    )

x = IntVar()
yaw_label = Label(yaw_frame, font="24")
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
    padx = 25
    )

y = IntVar()
pitch_label = Label(pitch_frame, font="24")
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

window.bind('<Motion>', lambda event: motion(event,pwm_list))
window.mainloop()
