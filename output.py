import json

# Variabel output_data merupaan variabel JSON yang berisi daftar device beserta pin yang digunakan.
# Untuk menambahkan device, tambahkan detail device kedalam JSON output_data sesuai dengan
# format yang ada.
#
# Note : Hindari iddevice yang sama, gunakan iddevice yang berbeda-beda untuk tiap device,dan juga
# pastikan iddevice tidak ada spasi !
output_data = '[{"iddevice":"ruangdepan","namadevice":"Ruang Depan","gpiopin":"1"},{"iddevice":"ruangtengah","namadevice":"Ruang Tengah","gpiopin":"2"},{"iddevice":"ruangbelakang","namadevice":"Ruang Belakang","gpiopin":"3"},{"iddevice":"ruangatas","namadevice":"Ruang Atas","gpiopin":"4"}]'
output_array = json.loads(output_data)