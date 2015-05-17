import RPi.GPIO as GPIO
import datetime
import time
from ledmatrix import LEDMatrix
import threading
 
delay = 0.000001
 
class LEDMatrixThreaded(LEDMatrix,threading.Thread): 
  def __init__(self):
    super(LEDMatrixThreaded, self).__init__()
    super(threading.Thread, self).__init__()

  def scan(self):
    head = self.row * (LEDMatrix.WIDTH / 8)
    index = head
    for byte in range (0, LEDMatrix.WIDTH / 8):
          pixels = self.displaybuf[index]
	  index += 1
	  pixels = pixels ^ LEDMatrix.mask
	  for bit in range (0,8):
	    GPIO.output(self.clock_pin,0)
            GPIO.output(self.red1_pin, pixels & (0x80 >> bit))
            GPIO.output(self.clock_pin,1)

    GPIO.output(self.oe_pin, 1)
    self.set_row(self.row)
    GPIO.output(self.latch_pin, 0)
    GPIO.output(self.latch_pin, 1)
    GPIO.output(self.latch_pin, 0)
    GPIO.output(self.oe_pin, 0)
    self.row = (self.row + 1) & 0x0F

  def swipeColumn(self):
    for i in range (0,8):
      time.sleep(0.1)
      self.moveLeft(0,16)

#for 16x64
  def swipeLeft(self):
    for i in range (0,64):
      time.sleep(0.1)
      self.moveLeft(0,16)


  def run(self):
    try:
      while True:
        self.scan()
        #print datetime.datetime.now()
        time.sleep(0.00001)
    except KeyboardInterrupt:
	exit(1)

myThread = LEDMatrixThreaded()
myThread.daemon = True
myThread.start()

while True:
    
    myThread.swipeLeft()
    myThread.displayLongMessage(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    myThread.displayLongMessage('Hello everybody! ',True)
    myThread.displayMessage('ABcd1234','efGH5678')
    myThread.swipeLeft()
