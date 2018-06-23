




from picamera import PiCamera
from time import sleep
from gpiozero import Button


button = Button(17)
camera = PiCamera()

camera.start_preview()
button.wait_for_press()
camera.start_recording('/home/pi/video.h264')
sleep(20)
camera.stop_recording()
camera.stop_preview()

