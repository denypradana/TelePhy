from time import sleep
import function
import login
import telegram

# Fungsi utama untuk menghandle semua perintah masuk
def handle(msg):

        # Mendapatkan ID user dan Perintah yang dikirimkan
        chat_id = msg['chat']['id']
        command = msg['text']

        """
        Memecah perintah masuk menjadi beberapa bagian 
        dengan berpatokan pada spasi
        """
        command_split = command.split(' ')

        # Mengambil indeks pertama dari perintah masuk yang telah dipecah
        command_cmd = command_split[0]

        """
        Menampilkan perintah yang diterima dari user beserta detail tanggal,
        waktu, serta ID user yang mengirimkan perintah
        """

        print("Pada "
                + str(function.tanggal())
                + " "+ str(function.jam())
                + ", user id "
                + str(chat_id)
                + " memberikan perintah '"
                + str(command) + "'.")

        # Melakukan aksi berdasarkan perintah yang diterima
        if command == '/start':
                bot.sendMessage(chat_id, 
                                "Selamat Datang di RB07-Pi, "
                                + "saya sebagai bot siap melayani anda. "
                                + "Ketik '/bantuan' untuk melihat bantuan "
                                + "atau ketik '/pwd Password_Anda' "
                                + " untuk login.")

        elif command == '/waktu':
                bot.sendMessage(chat_id, 
                                "Waktu server menunjukkan sekarang tanggal "
                                + function.tanggal()
                                + " dan pukul "
                                + function.jam()
                                + " WIB.")

        elif command == '/bantuan':
                function.bantuan(chat_id)

        elif command_cmd == '/pwd':
                if function.cekpass(chat_id, command_split[1]):
                        bot.sendMessage(chat_id, 
                        "Login Sukses.")

                else:
                        bot.sendMessage(chat_id, 
                                        "Maaf, password salah atau user "
                                        + "tidak terdaftar, "
                                        + "silahkan coba lagi.")

        elif command_cmd == '/on':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] != 'semua':
                                bot.sendMessage(chat_id,
                                                function.ondevice(
                                                        command_split[1]))

                        elif command_split[1] == 'semua':
                                function.onalldevice(chat_id)

                else:
                        bot.sendMessage(chat_id,
                                        "Anda belum login, harap login "
                                        + "dahulu dengan perintah "
                                        + "'/pwd Password_Anda'.")

        elif command_cmd == '/off':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] != 'semua':
                                bot.sendMessage(chat_id,
                                                function.offdevice(
                                                        command_split[1]))

                        elif command_split[1] == 'semua':
                                function.offalldevice(chat_id)

                else:
                        bot.sendMessage(chat_id,
                                        "Anda belum login, harap login "
                                        + "dahulu dengan perintah "
                                        + "'/pwd Password_Anda'.")

        elif command_cmd == '/info':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] == 'suhu':
                                bot.sendMessage(chat_id, 
                                                function.suhu())

                        else:
                                bot.sendMessage(chat_id, 
                                                "Sensor tidak ada.")

                else:
                        bot.sendMessage(chat_id, 
                                        "Anda belum login, harap login "
                                        + "dahulu dengan perintah "
                                        + "'/pwd Password_Anda'.")

        elif command_cmd == '/status':
                if function.cekpass(chat_id,login.password_sekarang):
                        if command_split[1] != 'semua':
                                bot.sendMessage(chat_id,
                                                function.statdevice(
                                                        command_split[1]))

                        elif command_split[1] == 'semua':
                                function.statalldevice(chat_id)

                else:
                        bot.sendMessage(chat_id, 
                                        "Anda belum login, harap login "
                                        + "dahulu dengan perintah "
                                        + "'/pwd Password_Anda'.")

        elif command_cmd == '/listdevice':
                if function.cekpass(chat_id,login.password_sekarang):
                        function.listdevice(chat_id)

                else:
                        bot.sendMessage(chat_id, 
                                        "Anda belum login, harap login "
                                        + "dahulu dengan perintah "
                                        + "'/pwd Password_Anda'.")

        else:
                bot.sendMessage(chat_id, 
                                "Perintah tidak ditemukan, gunakan "
                                + "perintah '/bantuan' untuk melihat "
                                + "bantuan yang ada.")

# Inisialisasi bot telegram
bot = telegram.bot
bot.message_loop(handle)

# Menampilkan Banner Program
print("################################################")
print("# TelePhy versi 1.0                            #")
print("# kontrol RaspberryPi anda dengan bot telegram #")
print("# https://github.com/denypradana/TelePhy       #")
print("#                                              #")
print("# dibuat oleh Deny Pradana                     #")
print("# https://denypradana.com                      #")
print("# email : dp@denypradana.com                   #")
print("################################################")

# Menampilkan keterangan kapan program mulai berjalan
print("Program mulai berjalan pada tanggal " 
        + function.tanggal() 
        + " pukul " 
        + function.jam() 
        + ".")

print("Menunggu Perintah...")

"""
Menjaga agar program tetap berjalan dan hanya akan berhenti
apabila ada perintah CTRL + C
"""

try:
        while 1:
                sleep(10)
                
except KeyboardInterrupt:
        print('Sambungan Terputus')