import gpiozero

# Inisialisasi GPIO, menentukan pin yang digunakan untuk output. 
RELAY1_PIN = 1
RELAY2_PIN = 2
RELAY3_PIN = 3
RELAY4_PIN = 4
RELAY5_PIN = 5
RELAY6_PIN = 6
RELAY7_PIN = 7
RELAY8_PIN = 8

# Setelah menentukan pin, kemudian menggunakan pin tersebut untuk output device
relay1 = gpiozero.OutputDevice(RELAY1_PIN, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(RELAY2_PIN, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(RELAY3_PIN, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(RELAY4_PIN, active_high=False, initial_value=False)
relay5 = gpiozero.OutputDevice(RELAY5_PIN, active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(RELAY6_PIN, active_high=False, initial_value=False)
relay7 = gpiozero.OutputDevice(RELAY7_PIN, active_high=False, initial_value=False)
relay8 = gpiozero.OutputDevice(RELAY8_PIN, active_high=False, initial_value=False)