import json

# Variabel user_data merupakan variabel JSON yang berisi daftar user id telegram user yang mempunyai
# akses ke sistem. Untuk menambahkan user telegram anda, anda bisa mengakses https://botostore.com/c/getmyid_bot/
# kemudian tambahkan user id dan password anda kedalam JSON user_data sesuai format yang ada
user_data = '[{"user_id":"463662008","password":"KucingImut"},{"user_id":"463662009","password":"KUCINGGARONG"}]'
user_array = json.loads(user_data)

# Variabel password_sekarang merupakan variabel yang menyimpan password user yang sedang aktif
# Sistem ini tidak dibuat multiuser, artinya hanya satu user yang bisa aktif pada satu waktu,
# sehingga apabila ada user lain yang ingin melakukan akses, wajib memasukkan passwordnya sendiri
# melalui menu /pwd.
password_sekarang = ""
