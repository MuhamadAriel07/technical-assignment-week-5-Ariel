import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 4

while True:
    humid, temperature = Adafruit_DHT.read(sensor, pin)

    if humid is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humid))
    else:
        print("Gagal membaca data sensor")
    time.sleep(1)
