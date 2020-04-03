import json

"""
Variabel user_data merupakan variabel JSON yang berisi daftar user id telegram
user yang mempunyai akses ke sistem. Untuk menambahkan user telegram anda, 
anda bisa mengakses https://botostore.com/c/getmyid_bot/ kemudian tambahkan 
user id dan password anda kedalam JSON user_data sesuai format yang ada

Note : Jangan menggunakan password yang sama dengan user lain !
"""

user_data = '[{"user_id":"123456789","password":"KucingImut"},\
            {"user_id":"123451234","password":"KUCINGGARONG"},\
            {"user_id":"123459876","password":"KucingGila"}]'

user_array = json.loads(user_data)

"""
Variabel password_sekarang merupakan variabel yang menyimpan password user 
yang sedang aktif. Sistem ini tidak dibuat multiuser, artinya hanya satu 
user yang bisa aktif pada satu waktu, sehingga apabila ada user lain yang 
ingin melakukan akses, wajib login dengan passwordnya sendiri melalui 
perintah /pwd.
"""

password_sekarang = ""