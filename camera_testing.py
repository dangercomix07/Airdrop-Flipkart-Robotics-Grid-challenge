import picamera
from time import sleep

camera = picamera.PiCamera()
camera.resolution = (1024,768)
camera.brightness = 60
camera.start_recording("/home/ameya/Documents/demo.h264")
camera.wait_recording(5)
camera.stop_recording()
camera.close()
print("goodbye")

