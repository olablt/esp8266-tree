# (micro)Python Christmas tree - Weekend project


## Flashing the firmware and code

Firmware can be dowbloaded here: http://micropython.org/download

```bash
cd /home/user/Projects/esp8266
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20171101-v1.9.3.bin
```

uploading the code

```bash
ampy --port /dev/ttyUSB0 put main.py
```


## Parts used

- https://makeblock.lt/led-juosta-rgb-5v-60-ledm-5050ws2812b-ip67-neopixel
- https://makeblock.lt/mikrovaldiklio-plokste-wemos-d1-mini-v2
- other cheap stuff found inside my house


## Video



[![video](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/youtube.png)](https://youtu.be/rH48stSCvnc)
<!-- [![video](/home/nemo/Projects/esp8266/firmwares/neopixel/images/youtube.png)](https://youtu.be/rH48stSCvnc) -->
<!-- [![video](https://i.ytimg.com/vi/rH48stSCvnc/hqdefault.jpg)](https://youtu.be/rH48stSCvnc) -->


## Images

<!-- https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/ -->




![](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/01.jpg)  |  ![](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/02.jpg)
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/03.jpg)  |  ![](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/04.jpg)
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/05.jpg)  |  ![](https://raw.githubusercontent.com/magveda/esp8266-tree/master/images/04.jpg)


<!-- 
![](/home/nemo/Projects/esp8266/firmwares/neopixel/images/01.jpg)  |  ![](/home/nemo/Projects/esp8266/firmwares/neopixel/images/02.jpg)
:-------------------------:|:-------------------------:
![](/home/nemo/Projects/esp8266/firmwares/neopixel/images/03.jpg)  |  ![](/home/nemo/Projects/esp8266/firmwares/neopixel/images/04.jpg)
:-------------------------:|:-------------------------:
![](/home/nemo/Projects/esp8266/firmwares/neopixel/images/05.jpg)  |  ![](/home/nemo/Projects/esp8266/firmwares/neopixel/images/04.jpg)
 -->