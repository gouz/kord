from machine import SPI, Pin
import sdcard, os

SD_MOUNT_PATH = '/sd'
FILE_PATH = 'sd/config.txt'

class MICROSD:
    def __init__(self):
        SPI_BUS = 1
        SCK_PIN = 14
        MOSI_PIN = 11
        MISO_PIN = 12
        CS_PIN = 13

        try:
            # Init SPI communication
            spi = SPI(SPI_BUS,sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))
            cs = Pin(CS_PIN)
            self.sd = sdcard.SDCard(spi, cs)
            
        except Exception as e:
            print('An error occurred:', e)

    def getConfig(self):
        hash_map = {}
        try: 
            os.mount(self.sd, SD_MOUNT_PATH)
            with open(FILE_PATH, "r") as file:
                # read the file content
                content = file.read()
                lines = content.strip().split('\n')
                for line in lines:
                    if '=' in line: 
                        key, value = line.split('=', 1)
                        hash_map[key] = value
            os.umount(SD_MOUNT_PATH)
        
        except Exception as e:
            print('An error occurred:', e)
        
        return hash_map