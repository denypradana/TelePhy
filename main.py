import time
import function
import login
import output
import telegram


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
                bot.sendMessage(chat_id, "Daftar Perintah : /start, /waktu, /bantuan.")
        elif command_cmd == '/pwd':
                if function.cekpass(chat_id, command_split[1]):
                        bot.sendMessage(chat_id, "Login Sukses.")
                else:
                        bot.sendMessage(chat_id, "Maaf, password salah atau user tidak terdaftar, silahkan coba lagi.")
        elif command_cmd == '/on':
                if function.cekpass(chat_id,login.password_sekarang):
                        bot.sendMessage(chat_id,function.ondevice(command_split[1]))
                        """
                        if command_split[1] == 'ruangdepan':
                                bot.sendMessage(chat_id, "Ruang Depan Hidup")
                                output.relay1.on()
                                output.RELAY1_STATUS = "ON"
                        elif command_split[1] == 'ruangtengah':
                                bot.sendMessage(chat_id, "Ruang Tengah Hidup")
                                output.relay2.on()
                                output.RELAY2_STATUS = "ON"
                        elif command_split[1] == 'ruangbelakang':
                                bot.sendMessage(chat_id, "Ruang Belakang Hidup")
                                output.relay3.on()
                                output.RELAY3_STATUS = "ON"
                        elif command_split[1] == 'ruangatas':
                                bot.sendMessage(chat_id, "Ruang Atas Hidup")
                                output.relay4.on()
                                output.RELAY4_STATUS = "ON"
                        elif command_split[1] == 'semua':
                                bot.sendMessage(chat_id, "Semua Ruangan Hidup")
                                output.relay1.on()
                                output.RELAY1_STATUS = "ON"
                                output.relay2.on()
                                output.RELAY2_STATUS = "ON"
                                output.relay3.on()
                                output.RELAY3_STATUS = "ON"
                                output.relay4.on()
                                output.RELAY4_STATUS = "ON"
                        else:
                                bot.sendMessage(chat_id, "Lokasi tidak diketahui.")
                        """
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/off':
                if function.cekpass(chat_id,login.password_sekarang):
                        bot.sendMessage(chat_id,function.ondevice(command_split[1]))
                        """
                        if command_split[1] == 'ruangdepan':
                                bot.sendMessage(chat_id, "Ruang Depan Mati")
                                output.relay1.off()
                                output.RELAY1_STATUS = "OFF"
                        elif command_split[1] == 'ruangtengah':
                                bot.sendMessage(chat_id, "Ruang Tengah Mati")
                                output.relay2.off()
                                output.RELAY2_STATUS = "OFF"
                        elif command_split[1] == 'ruangbelakang':
                                bot.sendMessage(chat_id, "Ruang Belakang Mati")
                                output.relay3.off()
                                output.RELAY3_STATUS = "OFF"
                        elif command_split[1] == 'ruangatas':
                                bot.sendMessage(chat_id, "Ruang Atas Mati")
                                output.relay4.off()
                                output.RELAY4_STATUS = "OFF"
                        elif command_split[1] == 'semua':
                                bot.sendMessage(chat_id, "Semua Ruangan Mati")
                                output.relay1.off()
                                output.RELAY1_STATUS = "OFF"
                                output.relay2.off()
                                output.RELAY2_STATUS = "OFF"
                                output.relay3.off()
                                output.RELAY3_STATUS = "OFF"
                                output.relay4.off()
                                output.RELAY4_STATUS = "OFF"
                        else:
                                bot.sendMessage(chat_id, "Lokasi tidak diketahui.")
                        """
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/info':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] == 'suhu':
                                bot.sendMessage(chat_id, function.suhu())
                        else:
                                bot.sendMessage(chat_id, "Lokasi tidak diketahui.")
                else:
                        bot.sendMessage(chat_id, "Anda belum login, harap login dahulu dengan perintah /pwd PasswordAnda.")
        elif command_cmd == '/status':
                bot.sendMessage(chat_id, "Ruang Depan : " + output.RELAY1_STATUS)
                time.sleep(1)
                bot.sendMessage(chat_id, "Ruang Tengah : " + output.RELAY2_STATUS)
                time.sleep(1)
                bot.sendMessage(chat_id, "Ruang Belakang : " + output.RELAY3_STATUS)
                time.sleep(1)
                bot.sendMessage(chat_id, "Ruang Atas : " + output.RELAY4_STATUS)
        else:
                bot.sendMessage(chat_id, "Perintah tidak ditemukan, gunakan /bantuan untuk melihat bantuan yang ada.")

# Inisialisasi bot telegram
bot = telegram.bot
bot.message_loop(handle)
print('################################################')
print('# TelePhy versi 0.1                            #')
print('# kontrol RaspberryPi anda dengan bot telegram #')
print('# dibuat oleh Deny Pradana                     #')
print('#                                              #')
print('# https://denypradana.com                      #')
print('# email : dp@denypradana.com                   #')
print('################################################')
print('Menunggu Perintah...')

try:
        while 1:
                time.sleep(10)
except KeyboardInterrupt:
        print('Sambungan Terputus')
