from datetime import datetime
from signal import pause
import input
import output
import login
import gpiozero
import json

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

# Fungsi untuk menghidupkan device
def ondevice(devid):
        for element in output.output_array:
                if element['iddevice'] == devid:
                        output.DEVICE_PIN = int(element['gpiopin'])
                        #deviceout = gpiozero.OutputDevice(DEVICE_PIN, active_high=False, initial_value=False)
                        output.deviceout.on()
                        pause()
                        return element['namadevice'] + " Hidup pada pin " + str(output.DEVICE_PIN)
        else:
                return "ID Device " + str(devid) + " tidak ditemukan"

# Fungsi untuk mematikan device
def offdevice(devid):
        for element in output.output_array:
                if element['iddevice'] == devid:
                        output.DEVICE_PIN = int(element['gpiopin'])
                        #deviceout = gpiozero.OutputDevice(DEVICE_PIN, active_high=False, initial_value=False)
                        output.deviceout.off()
                        
                        return element['namadevice'] + " Mati pada pin " + str(output.DEVICE_PIN)
        else:
                return "ID Device " + str(devid) + " tidak ditemukan"
