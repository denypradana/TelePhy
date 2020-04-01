from time import sleep

import function
import login
import telegram

# Fungsi Utama
def handle(msg):

        chat_id = msg['chat']['id']
        command = msg['text']

        # Memecah perintah masuk menjadi beberapa bagian dengan berpatokan pada spasi
        command_split = command.split(' ')
        command_cmd = command_split[0]

        # Menampilkan perintah yang diterima dari user
        print('Perintah Masuk : %s' % command)

        # Melakukan aksi berdasarkan perintah yang diterima
        if command == '/start':
                bot.sendMessage(chat_id, "Selamat Datang di RB07-Pi, saya sebagai bot siap melayani anda. Ketik /bantuan untuk melihat bantuan atau ketik /pwd PasswordAnda untuk login.")
        elif command == '/waktu':
                bot.sendMessage(chat_id, "Waktu server menunjukkan sekarang tanggal " + function.tanggal() + " dan pukul " + function.jam() + " WIB.")
        elif command == '/bantuan':
                bot.sendMessage(chat_id, "Perintah /start -> untuk menampilkan pesan selamat datang.")
                bot.sendMessage(chat_id, "Perintah /waktu -> untuk menampilkan tanggal dan waktu server.")
                bot.sendMessage(chat_id, "Perintah /bantuan -> untuk menampilkan pesan-pesan bantuan ini.")
                bot.sendMessage(chat_id, "Perintah /pwd -> untuk login kedalam sistem. Cara penggunaan : '/pwd Password_Anda'.")
                bot.sendMessage(chat_id, "Perintah /listdevice -> untuk menampilkan daftar ID Device beserta nama dan lokasi pin device.")
                bot.sendMessage(chat_id, "Perintah /on -> untuk menghidupkan device. Cara penggunaannya, untuk menghidupkan device tertentu perintahnya : '/on ID_Device' dan untuk menghidupkan semua device, perintahnya : '/on semua'.")
                bot.sendMessage(chat_id, "Perintah /off -> untuk mematikan device. Cara penggunaannya, untuk mematikan device tertentu perintahnya : '/off ID_Device' dan untuk mematikan semua device, perintahnya : '/off semua'.")
                bot.sendMessage(chat_id, "Perintah /status -> untuk melihat status device. Cara penggunaannya, untuk melihat status device tertentu perintahnya : '/status ID_Device' dan untuk melihat status semua device, perintahnya : '/status semua'.")
                bot.sendMessage(chat_id, "Perintah /info -> untuk membaca sensor. Cara penggunaan :'/info TipeSensor'. (Tipe Sensor yang tersedia : 'suhu').")
        elif command_cmd == '/pwd':
                if function.cekpass(chat_id, command_split[1]):
                        bot.sendMessage(chat_id, "Login Sukses.")
                else:
                        bot.sendMessage(chat_id, "Maaf, password salah atau user tidak terdaftar, silahkan coba lagi.")
        elif command_cmd == '/on':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] != 'semua':
                                bot.sendMessage(chat_id,function.ondevice(command_split[1]))
                        elif command_split[1] == 'semua':
                                function.onalldevice(chat_id)
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/off':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] != 'semua':
                                bot.sendMessage(chat_id,function.offdevice(command_split[1]))
                        elif command_split[1] == 'semua':
                                function.offalldevice(chat_id)
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/info':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] == 'suhu':
                                bot.sendMessage(chat_id, function.suhu())
                        else:
                                bot.sendMessage(chat_id, "Sensor tidak ada.")
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/status':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] != 'semua':
                                bot.sendMessage(chat_id,function.statdevice(command_split[1]))
                        elif command_split[1] == 'semua':
                                function.statalldevice(chat_id)
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/listdevice':
                if function.cekpass(chat_id,login.password_sekarang):
                        function.listdevice(chat_id)
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        else:
                bot.sendMessage(chat_id, "Perintah tidak ditemukan, gunakan /bantuan untuk melihat bantuan yang ada.")

# Inisialisasi bot telegram
bot = telegram.bot
bot.message_loop(handle)
print('################################################')
print('# TelePhy versi 0.2                            #')
print('# kontrol RaspberryPi anda dengan bot telegram #')
print('# dibuat oleh Deny Pradana                     #')
print('#                                              #')
print('# https://denypradana.com                      #')
print('# email : dp@denypradana.com                   #')
print('################################################')
print('Menunggu Perintah...')

try:
        while 1:
                sleep(10)
except KeyboardInterrupt:
        print('Sambungan Terputus')