# Seeed_Python_Ds18b20

[DS18B20 Waterproof Temperature Sensor](https://www.seeedstudio.com/One-Wire-Temperature-Sensor-p-1235.html) is a digital sensor which can reach the digital data resolution up to 12 bits and has ±0.5°C accuracy from -10°C to +85°C. It includes an analog-to-digital converter to convert the analog signal to the digital output with the resolution up to 
12 bits.

![](https://static-cdn.seeedstudio.site/media/catalog/product/cache/9d0ce51a71ce6a79dfa2a98d65a0f0bd/h/t/httpsstatics3.seeedstudio.comimagesproductonewiretempsensor.jpg)

## Dependencies

This driver depends on:
- [***grove.py***](https://github.com/Seeed-Studio/grove.py)

This is easy to install with the following command.

```python
pip3 install Seeed-grove.py
```

### Installing from PyPI

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally from PyPI. To install for current user:

```
pip3 install seeed-python-Ds18b20
```

To install system-wide (this may be required in some cases):

```
sudo pip3 install seeed-python-Ds18b20
```

if you want to update the driver locally from PyPI. you can use:

```
pip3 install --upgrade seeed-python-Ds18b20
```

## Usage

connect Ds18b20 to D5 at BaseHat.

```python
import seeed_ds18b20
import time

def main():
    DS18B20 = seeed_ds18b20.grove_ds18b20()
    print("Please use Ctrl C to quit")
    while True:
        temp_c,temp_f = DS18B20.read_temp
        print('temp_c %.2f C   temp_f %.2f F' % (temp_c,temp_f),end=" ")
        print('\r', end='')
        time.sleep(0.5)

if __name__ == "__main__":
    main()   
```

## API Reference

- uint16_t,uint16_t read_temp(void):return temperature

```python
temp_c,temp_f = DS18B20.read_temp
```
----

This software is written by seeed studio<br>
and is licensed under [The MIT License](http://opensource.org/licenses/mit-license.php). Check License.txt for more information.<br>

Contributing to this software is warmly welcomed. You can do this basically by<br>
[forking](https://help.github.com/articles/fork-a-repo), committing modifications and then [pulling requests](https://help.github.com/articles/using-pull-requests) (follow the links above<br>
for operating guide). Adding change log and your contact into file header is encouraged.<br>
Thanks for your contribution.

Seeed Studio is an open hardware facilitation company based in Shenzhen, China. <br>
Benefiting from local manufacture power and convenient global logistic system, <br>
we integrate resources to serve new era of innovation. Seeed also works with <br>
global distributors and partners to push open hardware movement.<br>


[![Analytics](https://ga-beacon.appspot.com/UA-46589105-3/Grove_LED_Bar)](https://github.com/igrigorik/ga-beacon)