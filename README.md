# ledmatrix
Raspberry Pi Python library to control 16x64 LED matrix panel using Driver IC : 74HC245 74HC595  74HC138 74HC04 APM4953

After successfully testing the single color 16hx64 LED Matrix with an arduino, I wanted to control the display with a Raspberry Pi B+ and an easy to use python library. I could not find one so I used the ultrathin libray from Seeed to understand how the display worked, and I first ported the code to python and made improvments along the way such as an object oriented code and multi-threaded refresh.

The LEDs have to be refreshed constantly so you may experience a bit of flickering depending on the load of the OS and inherent interruptions compared to an Arduino.

To use the library within your project, import and instantiate LEDMatix. There are default port assigned by default but you may change them to suit your project. 

This library was inspired by the Arduino library Ultrathin LED Matrix Library https://github.com/Seeed-Studio/Ultrathin_LED_Matrix
