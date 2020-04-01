import json

output_data = '[{"iddevice":"ruangdepan","namadevice":"Ruang Depan","status":"OFF","gpiopin":"28"},{"iddevice":"ruangtengah","namadevice":"Ruang Tengah","status":"OFF","gpiopin":"3"},{"iddevice":"ruangbelakang","namadevice":"Ruang Belakang","status":"OFF","gpiopin":"5"},{"iddevice":"ruangatas","namadevice":"Ruang Atas","status":"OFF","gpiopin":"7"}]'
output_array = json.loads(output_data)