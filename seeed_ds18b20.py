#!/usr/bin/python3
# -*- coding:utf-8 -*-
import glob
import time
from grove.gpio import GPIO
# This relies on the driver written by siddacious and can be found at:
# https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/Raspberry_Pi_DS18B20_Temperature_Sensing/thermometer.py

rev_to_dtoverlay = {
    1 :"dtoverlay=w1-gpio,gpiopin=5 >> /boot/config.txt",
    2 :"dtoverlay=w1-gpio,gpiopin=5 >> /boot/config.txt",
    3 :"dtoverlay=w1-gpio,gpiopin=5 >> /boot/config.txt",
    4 :"dtoverlay=w1-gpio,gpiopin=5 >> /boot/config.txt",
}

class grove_ds18b20(object):
    def __init__(self):
        rev = GPIO.RPI_REVISION
        self.base_dir = '/sys/bus/w1/devices/'
        try:
            self.device_folder = glob.glob(self.base_dir + '28*')[0]
        except:
                meg = "\n\
#############################################################################\
\n\
\n\
Please use \'sudo sh -c \"echo %s\"\' then reboot to enable the w1\
\n\
\n\
#############################################################################"%(rev_to_dtoverlay[rev])
                raise OSError (None, meg)
        self.device_file = self.device_folder + '/w1_slave'
    # read raw data by using /sys/bus
    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    # read temperature that after convert
    @property
    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f

def main():
    DS18B20 = grove_ds18b20()
    print("Please use Ctrl C to quit")
    while True:
        temp_c,temp_f = DS18B20.read_temp
        print('temp_c %.2f C   temp_f %.2f F' % (temp_c,temp_f),end=" ")
        print('\r', end='')
        time.sleep(0.5)

if __name__ == "__main__":
    main()     