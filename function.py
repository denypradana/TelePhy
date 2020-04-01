from datetime import datetime
import RPi.GPIO as GPIO
import input
import output
import login
import telegram

# Menyembunyikan warning dari GPIO
GPIO.setwarnings(False)

# Inisialisasi bit telegram
bot = telegram.bot

# Fungsi untuk membaca suhu dari sensor yang ada pada modul input
def suhu():
        humidity, temperature = input.Adafruit_DHT.read_retry(input.DHT1_SENSOR, input.DHT1_PIN)
        infodht = 'Suhu Sekarang={0:0.1f} C  Kelembaban={1:0.1f}%'.format(temperature, humidity)
        return infodht

# Fungsi untuk mendapatkan tanggal pada server
def tanggal():
        sekarang = datetime.now()
        tanggal = sekarang.strftime('%d-%m-%Y')
        return tanggal

# Fungsi untuk mendapatkan jam pada server
def jam():
        sekarang = datetime.now()
        jam = sekarang.strftime('%H:%M:%S')
        return jam

# Fungsi untuk pengecekan password
def cekpass(uid,pwd):
        for element in login.user_array:
                if element['user_id'] == str(uid):
                        if element['password'] == pwd:
                                login.password_sekarang = pwd
                                return True
        else:
                login.password_sekarang = ""
                return False

# Fungsi untuk menghidupkan device tertentu
def ondevice(devid):
        for element in output.output_array:
                if element['iddevice'] == devid:
                        DEVICE_PIN = int(element['gpiopin'])
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(DEVICE_PIN,GPIO.OUT)

                        # Untuk device lain selain relay, ganti GPIO.LOW menjadi GPIO.HIGH
                        GPIO.output(DEVICE_PIN,GPIO.LOW)
                        return element['namadevice'] + " Hidup"
        else:
                return "ID Device " + str(devid) + " tidak ditemukan"

# Fungsi untuk mematikan device tertentu
def offdevice(devid):
        for element in output.output_array:
                if element['iddevice'] == devid:
                        DEVICE_PIN = int(element['gpiopin'])
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(DEVICE_PIN,GPIO.OUT)

                        # Untuk device lain selain relay, ganti GPIO.HIGH menjadi GPIO.LOW
                        GPIO.output(DEVICE_PIN,GPIO.HIGH)
                        return element['namadevice'] + " Mati"
        else:
                return "ID Device " + str(devid) + " tidak ditemukan"

# Fungsi untuk menghidupkan semua device
def onalldevice(chat_id):
        for element in output.output_array:
                DEVICE_PIN = int(element['gpiopin'])
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(DEVICE_PIN,GPIO.OUT)

                # Untuk device lain selain relay, ganti GPIO.LOW menjadi GPIO.HIGH
                GPIO.output(DEVICE_PIN,GPIO.LOW)
                bot.sendMessage(chat_id,element['namadevice'] + " Hidup")

# Fungsi untuk mematikan semua device
def offalldevice(chat_id):
        for element in output.output_array:
                DEVICE_PIN = int(element['gpiopin'])
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(DEVICE_PIN,GPIO.OUT)

                # Untuk device lain selain relay, ganti GPIO.HIGH menjadi GPIO.LOW
                GPIO.output(DEVICE_PIN,GPIO.HIGH)
                bot.sendMessage(chat_id,element['namadevice'] + " Mati")

# Fungsi untuk mendapatkan status device tertentu
def statdevice(devid):
        for element in output.output_array:
                if element['iddevice'] == devid:
                        DEVICE_PIN = int(element['gpiopin'])
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(DEVICE_PIN,GPIO.OUT)
                        state = GPIO.input(DEVICE_PIN)

                        # Untuk device lain selain relay, ganti Mati menjadi Hidup dan sebaliknya
                        if state:
                                return element['namadevice'] + " dalam keadaan Mati"
                        else:
                                return element['namadevice'] + " dalam keadaan Hidup"
        else:
                return "ID Device " + str(devid) + " tidak ditemukan"

# Fungsi untuk mendapatkan status semua device
def statalldevice(chat_id):
        for element in output.output_array:
                DEVICE_PIN = int(element['gpiopin'])
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(DEVICE_PIN,GPIO.OUT)
                state = GPIO.input(DEVICE_PIN)

                # Untuk device lain selain relay, ganti Mati menjadi Hidup dan sebaliknya
                if state:
                        bot.sendMessage(chat_id,element['namadevice'] + " dalam keadaan Mati")
                else:
                        bot.sendMessage(chat_id,element['namadevice'] + " dalam keadaan Hidup")

# Fungsi untuk mendapatkan list semua device
def listdevice(chat_id):
        for element in output.output_array:
                bot.sendMessage(chat_id,"ID Device : " + element['iddevice'] + ". Nama Device :" + element['namadevice'] + " & Lokasi Device di GPIO" + element['gpiopin'])