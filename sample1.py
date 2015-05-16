from ledmatrix import LEDMatrix
import datetime

while True:
    red1_pin = 17
    clock_pin = 3
    a_pin = 7
    b_pin = 8
    c_pin = 9
    d_pin = 10
    latch_pin = 4
    oe_pin = 2

    ledmatrix = LEDMatrix()
    #ledmatrix = LEDMatrix(red1_pin, clock_pin, a_pin, b_pin, c_pin, d_pin, latch_pin, oe_pin)
    ledmatrix.swipeLeft()
    ledmatrix.displayLongMessage(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    ledmatrix.displayMessage('ABcd1234','efGH5678')
    ledmatrix.swipeLeft()
    ledmatrix.displayLongMessage('Raspberry Pi LED Matrix with Python ',True)
    ledmatrix.swipeLeft()
    ledmatrix.drawRect(0,0,10,12,1)
    ledmatrix.drawCharacter(48,0,71)
    ledmatrix.drawCharacter(56,0,55)
    ledmatrix.drawDigital(32,0,2)
    ledmatrix.drawDigital(40,0,4)

