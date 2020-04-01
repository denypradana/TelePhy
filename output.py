import json

output_data = '[{"iddevice":"ruangdepan","namadevice":"Ruang Depan","status":"OFF","gpiopin":"1"},{"iddevice":"ruangtengah","namadevice":"Ruang Tengah","status":"OFF","gpiopin":"2"},{"iddevice":"ruangbelakang","namadevice":"Ruang Belakang","status":"OFF","gpiopin":"3"},{"iddevice":"ruangatas","namadevice":"Ruang Atas","status":"OFF","gpiopin":"4"}]'
output_array = json.loads(output_data)