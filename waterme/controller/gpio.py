from time import sleep 
import RPi.GPIO as GPIO

def setup_board():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

def setup_device(device_pin: int, pin_config = GPIO.OUT):
    GPIO.setup(device_pin, GPIO.OUT)

def device_off(device_pin: int):
    GPIO.output(device_pin, 0)
    
def device_on(device_pin: int):
    GPIO.input(device_pin, 1)
