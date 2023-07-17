import RPi.GPIO as GPIO
import time

def setup(pin,frequency):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
    pwm=GPIO.PWM(pin,frequency)
    pwm.start(0)
    return pwm

def sweep(pwm_list,start,stop,increment):
    for i in range(start,stop,increment):
        duty_cycle=1/18*i+2
        for pwm in pwm_list:
            pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(sleep_timer)

# Setting up Program
GPIO.setmode(GPIO.BCM)
sleep_timer=0.35
frequency=50
yaw_pwm = setup(23,frequency)
pitch_pwm = setup(24,frequency)
pwm_list = [yaw_pwm,pitch_pwm]

# Sweeping Servo Range of Motion
sweep(pwm_list,0,180,30)
sweep(pwm_list,180,-30,-30)

# Stopping PWM outputs
yaw_pwm.stop()
pitch_pwm.stop()
GPIO.cleanup()
