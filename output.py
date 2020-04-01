import json
import gpiozero

output_data = '[{"iddevice":"ruangdepan","namadevice":"Ruang Depan","status":"OFF","gpiopin":"1"},{"iddevice":"ruangtengah","namadevice":"Ruang Tengah","status":"OFF","gpiopin":"2"},{"iddevice":"ruangbelakang","namadevice":"Ruang Belakang","status":"OFF","gpiopin":"3"},{"iddevice":"ruangatas","namadevice":"Ruang Atas","status":"OFF","gpiopin":"4"}]'
output_array = json.loads(output_data)
# Inisialisasi GPIO, menentukan pin yang digunakan untuk output. 
"""
RELAY1_PIN = 1
RELAY2_PIN = 2
RELAY3_PIN = 3
RELAY4_PIN = 4
RELAY5_PIN = 5
RELAY6_PIN = 6
RELAY7_PIN = 7
RELAY8_PIN = 8

# Variabel untuk menampung status masing-masing pin
RELAY1_STATUS="OFF"
RELAY2_STATUS="OFF"
RELAY3_STATUS="OFF"
RELAY4_STATUS="OFF"
RELAY5_STATUS="OFF"
RELAY6_STATUS="OFF"
RELAY7_STATUS="OFF"
RELAY8_STATUS="OFF"

# Setelah menentukan pin, kemudian menggunakan pin tersebut untuk output device
relay1 = gpiozero.OutputDevice(RELAY1_PIN, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(RELAY2_PIN, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(RELAY3_PIN, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(RELAY4_PIN, active_high=False, initial_value=False)
relay5 = gpiozero.OutputDevice(RELAY5_PIN, active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(RELAY6_PIN, active_high=False, initial_value=False)
relay7 = gpiozero.OutputDevice(RELAY7_PIN, active_high=False, initial_value=False)
relay8 = gpiozero.OutputDevice(RELAY8_PIN, active_high=False, initial_value=False)
"""