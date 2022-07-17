1. Wiring diagram untuk sensor tersebut menggunakan fritzing ( upload dalam MD files screenshot wiring diagram tersebut )
2. Script sensor.py dan sebuah fungsi untuk mengambil data dari sensor tersebut
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(0)
3. Sebuah script utama main.py yang terdiri dari sebuah logic sederhana yang menjawab sebuah use case sederhana ( jelaskan use case tersebut dalam MD files! )
4. (Optional) Ambil sekitar 5 - 10 sample data dan tampilkan dalam sebuah grafik matplotlib dan screenshot hasil tersebut dan upload pada MD files.