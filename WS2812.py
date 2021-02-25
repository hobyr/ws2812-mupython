# my own WS2812 LEDs driver
# Uses SPI bus to transmit the data to the LEDs

from pyb import SPI

class WS2812:
    def __init__(self, bus=1, led_count=1):
       self.device = SPI(bus, SPI.MASTER, baudrate=6400000, polarity=0, phase=1)
       self.buf_bytes = (0xC0, 0xF0)
       self.led_count = led_count
       self.data_bytes = bytearray(24 * led_count)

    def update_buffer(self, data):
        bufferBytes = self.buf_bytes
        bytesToSend = self.data_bytes

        index = 0
        for red, green, blue in data:
            bytesToSend[index+0]  = bufferBytes[green >> 7 & 0x01]
            bytesToSend[index+1]  = bufferBytes[green >> 6 & 0x01]
            bytesToSend[index+2]  = bufferBytes[green >> 5 & 0x01]
            bytesToSend[index+3]  = bufferBytes[green >> 4 & 0x01]
            bytesToSend[index+4]  = bufferBytes[green >> 3 & 0x01]
            bytesToSend[index+5]  = bufferBytes[green >> 2 & 0x01]
            bytesToSend[index+6]  = bufferBytes[green >> 1 & 0x01]
            bytesToSend[index+7]  = bufferBytes[green >> 0 & 0x01]

            bytesToSend[index+8]  = bufferBytes[red >> 7 & 0x01]
            bytesToSend[index+9]  = bufferBytes[red >> 6 & 0x01]
            bytesToSend[index+10] = bufferBytes[red >> 5 & 0x01]
            bytesToSend[index+11] = bufferBytes[red >> 4 & 0x01]
            bytesToSend[index+12] = bufferBytes[red >> 3 & 0x01]
            bytesToSend[index+13] = bufferBytes[red >> 2 & 0x01]
            bytesToSend[index+14] = bufferBytes[red >> 1 & 0x01]
            bytesToSend[index+15] = bufferBytes[red >> 0 & 0x01]

            bytesToSend[index+16] = bufferBytes[blue >> 7 & 0x01]
            bytesToSend[index+17] = bufferBytes[blue >> 6 & 0x01]
            bytesToSend[index+18] = bufferBytes[blue >> 5 & 0x01]
            bytesToSend[index+19] = bufferBytes[blue >> 4 & 0x01]
            bytesToSend[index+20] = bufferBytes[blue >> 3 & 0x01]
            bytesToSend[index+21] = bufferBytes[blue >> 2 & 0x01]
            bytesToSend[index+22] = bufferBytes[blue >> 1 & 0x01]
            bytesToSend[index+23] = bufferBytes[blue >> 0 & 0x01]

            index += 24

    def show(self, data):
        self.update_buffer(data)
        self.device.send(self.data_bytes)

