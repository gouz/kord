from machine import SPI, Pin
import sdcard, os

class MICROSD:
    def __init__(self):
        SPI_BUS = 1
        SCK_PIN = 14
        MOSI_PIN = 11
        MISO_PIN = 12
        CS_PIN = 13
        SD_MOUNT_PATH = '/sd'
        FILE_PATH = 'sd/config.txt'

        try:
            # Init SPI communication
            spi = SPI(SPI_BUS,sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))
            cs = Pin(CS_PIN)
            sd = sdcard.SDCard(spi, cs)
            # Mount microSD card
            os.mount(sd, SD_MOUNT_PATH)
            # List files on the microSD card
            print(os.listdir(SD_MOUNT_PATH))
            
        except Exception as e:
            print('An error occurred:', e)