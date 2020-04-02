# TelePhy ver 1.0
Kontrol Raspberry Pi anda menggunakan Bot Telegram.

TelePhy dibuat menggunakan bahasa pemrograman Python 3, jadi pastikan anda menggunakan requirements yang dibuat untuk Python 3.

## Install Requirements
Bila RaspberryPi anda menggunakan OS Raspbian, anda bisa menginstal requirements dengan cara sebagai berikut :

```
pi@raspberrypi:~$ sudo apt update
pi@raspberrypi:~$ sudo pip3 install telepot
```

Untuk OS lain, anda bisa menginstall requirements dengan menggunakan perintah berikut :

```
pi@raspberrypi:~/TelePhy $ sudo pip3 install -r requirements.txt 
```

**Note :** Bila anda menggunakan sensor DHT untuk mengukur suhu dan kelembaban, anda harus menginstall library khusus dari Adafruit, caranya adalah sebagai berikut :

```
pi@raspberrypi:~$ sudo apt-get update
pi@raspberrypi:~$ sudo apt-get install build-essential python3-dev

pi@raspberrypi:~$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
pi@raspberrypi:~$ cd Adafruit_Python_DHT

pi@raspberrypi:~/Adafruit_Python_DHT $ sudo python3 setup.py install
```

## Menjalankan TelePhy
Untuk menjalankan TelePhy, gunakan perintah berikut :

```
pi@raspberrypi:~/TelePhy $ python3 main.py
```

## Konfigurasi TelePhy
File Konfigurasi TelePhy terdapat pada beberapa file sesuai dengan konfigurasinya, edit file-file berikut ini untuk mengganti konfigurasi :

**Note :** Lakukan backup terlebih dahulu sebelum melakukan perubahan konfigurasi !

- Untuk menambah, menghapus, mengedit user --> login.py
- Untuk menambah, menghapus, mengedit sensor --> input.py
- Untuk menambah, menghapus, mengedit device --> output.py
- Untuk konfigurasi bot telegram --> telegram.py