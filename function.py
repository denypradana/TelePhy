from datetime import datetime
import RPi.GPIO as GPIO
import input
import output
import login
import telegram

# Menyembunyikan warning dari GPIO
GPIO.setwarnings(False)

# Inisialisasi bot telegram
bot = telegram.bot

# Fungsi untuk membaca suhu dari sensor yang ada pada modul input
def suhu():
        humidity, temperature = input.Adafruit_DHT.read_retry(
                                input.DHT1_SENSOR, input.DHT1_PIN)

        infodht = 'Suhu Sekarang={0:0.1f} C  Kelembaban={1:0.1f}%'.format(
                                temperature, humidity)

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

                        """
                        Untuk device lain selain relay, ganti GPIO.LOW 
                        menjadi GPIO.HIGH
                        """

                        GPIO.output(DEVICE_PIN,GPIO.LOW)

                        return statdevice(devid)

        else:
                return "ID Device "\
                        + str(devid)\
                        + " tidak ditemukan"

# Fungsi untuk mematikan device tertentu
def offdevice(devid):
        for element in output.output_array:

                if element['iddevice'] == devid:
                        DEVICE_PIN = int(element['gpiopin'])
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(DEVICE_PIN,GPIO.OUT)

                        """
                        Untuk device lain selain relay, ganti GPIO.HIGH
                        menjadi GPIO.LOW
                        """

                        GPIO.output(DEVICE_PIN,GPIO.HIGH)

                        return statdevice(devid)

        else:
                return "ID Device "\
                        + str(devid)\
                        + " tidak ditemukan"

# Fungsi untuk menghidupkan semua device
def onalldevice(chat_id):
        for element in output.output_array:

                DEVICE_PIN = int(element['gpiopin'])
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(DEVICE_PIN,GPIO.OUT)

                """
                Untuk device lain selain relay, ganti GPIO.LOW
                menjadi GPIO.HIGH
                """

                GPIO.output(DEVICE_PIN,GPIO.LOW)

                bot.sendMessage(chat_id,
                                statdevice(element['iddevice']))

# Fungsi untuk mematikan semua device
def offalldevice(chat_id):
        for element in output.output_array:

                DEVICE_PIN = int(element['gpiopin'])
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(DEVICE_PIN,GPIO.OUT)

                """
                Untuk device lain selain relay, ganti GPIO.HIGH
                menjadi GPIO.LOW
                """

                GPIO.output(DEVICE_PIN,GPIO.HIGH)

                bot.sendMessage(chat_id,
                                statdevice(element['iddevice']))

# Fungsi untuk mendapatkan status device tertentu
def statdevice(devid):
        for element in output.output_array:

                if element['iddevice'] == devid:
                        DEVICE_PIN = int(element['gpiopin'])
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(DEVICE_PIN,GPIO.OUT)
                        state = GPIO.input(DEVICE_PIN)

                        """
                        Untuk device lain selain relay, ganti Mati menjadi 
                        Hidup dan sebaliknya
                        """

                        if state: 
                                return element['namadevice']\
                                        + " dalam keadaan Mati"
                                        
                        else:
                                return element['namadevice']\
                                        + " dalam keadaan Hidup"

        else:
                return "ID Device "\
                        + str(devid)\
                        + " tidak ditemukan"

# Fungsi untuk mendapatkan status semua device
def statalldevice(chat_id):
        for element in output.output_array:

                DEVICE_PIN = int(element['gpiopin'])
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(DEVICE_PIN,GPIO.OUT)
                state = GPIO.input(DEVICE_PIN)

                """
                Untuk device lain selain relay, ganti Mati menjadi Hidup dan
                sebaliknya
                """
                if state:
                        bot.sendMessage(chat_id,
                                        element['namadevice']
                                        + " dalam keadaan Mati")

                else:
                        bot.sendMessage(chat_id,
                                        element['namadevice']
                                        + " dalam keadaan Hidup")

# Fungsi untuk mendapatkan list semua device
def listdevice(chat_id):
        for element in output.output_array:

                bot.sendMessage(chat_id,
                                "ID Device : "
                                + element['iddevice']
                                + ". Nama Device : "
                                + element['namadevice']
                                + " & Lokasi Device di GPIO"
                                + element['gpiopin'])

# Fungsi untuk mengirimkan daftar bantuan
def bantuan(chat_id):
        bot.sendMessage(chat_id,
                        "Perintah /start -> "
                        + "untuk menampilkan pesan selamat datang.")

        bot.sendMessage(chat_id, 
                        "Perintah /waktu -> "
                        + "untuk menampilkan tanggal "
                        + "dan waktu server.")

        bot.sendMessage(chat_id, 
                        "Perintah /bantuan -> "
                        + "untuk menampilkan pesan-pesan "
                        + "bantuan ini.")

        bot.sendMessage(chat_id, 
                        "Perintah /pwd -> "
                        + "untuk login kedalam sistem. "
                        + "Cara penggunaan : '/pwd Password_Anda'.")

        bot.sendMessage(chat_id, 
                        "Perintah /listdevice -> "
                        + "untuk menampilkan daftar ID Device "
                        + "beserta nama dan lokasi pin device.")

        bot.sendMessage(chat_id, 
                        "Perintah /on -> "
                        + "untuk menghidupkan device. "
                        + "Cara penggunaannya, untuk menghidupkan "
                        + "device tertentu, perintahnya : "
                        + "'/on ID_Device' dan untuk menghidupkan "
                        + "semua device, perintahnya : '/on semua'.")

        bot.sendMessage(chat_id, 
                        "Perintah /off -> "
                        + "untuk mematikan device. "
                        + "Cara penggunaannya, untuk mematikan "
                        + "device tertentu, perintahnya : "
                        + "'/off ID_Device' dan untuk mematikan "
                        + "semua device, perintahnya : '/off semua'.")

        bot.sendMessage(chat_id, 
                        "Perintah /status -> "
                        + "untuk melihat status device. "
                        + "Cara penggunaannya, untuk melihat status "
                        + "device tertentu, perintahnya : "
                        + "'/status ID_Device' dan untuk melihat "
                        + "status semua device, perintahnya : "
                        + "'/status semua'.")

        bot.sendMessage(chat_id, 
                        "Perintah /info -> "
                        + "untuk membaca sensor. Cara penggunaan : "
                        + "'/info TipeSensor'. (Tipe Sensor yang "
                        + "tersedia : 'suhu').")