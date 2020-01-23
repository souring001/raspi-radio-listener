import socket
import time
import RPi.GPIO as GPIO

BUTTON_PIN = 9
IP = '192.168.170.58'
PORT = 51452
status = 0

def callback(channel):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        s.sendall(status.to_bytes(2, 'big'))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=callback, bouncetime=300)

while True:
    time.sleep(1)
