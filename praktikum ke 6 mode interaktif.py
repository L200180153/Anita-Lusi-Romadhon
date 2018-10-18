Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\win10\Documents\praktikum 6.py ==============
>>> ## Kegiatan 1
>>> Nama_panjang
'Anita Lusi Romadhon'
>>> Nama_singkat
'A.L.Romadhon'
>>> NIM
'L200180153'
>>> Alamat
'Sragen'
>>> Tempat_tinggal
'Nila Sari'
>>> Fakultas
'FKI'
>>> Prodi
'Informatika'
>>> Kelas
'D'
>>> TTl
'Sragen,02Januari2000'
>>> Hobi
'membaca'
>>> 
============== RESTART: C:\Users\win10\Documents\praktikum 6.py ==============
>>> ## Kegiatan 2
>>> Nama
'Anita Lusi Romadhon'
>>> Tanggal_lahir
'02 Januari 2000'
>>> Nama_singkat
'A.L.Romadhon'
>>> Username
'A022000'
>>> Password
'Ani041'
>>> 
>>> ## Kegiatan 3
>>> Nama ='Anita Lusi Romadhon'
>>> NIM ='L200180153'
>>> x='1' + NIM[7:] #didalam string digabungkan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print(x) # menampilkan variabel x
1153
>>> a = int(x) # konversi string ke integer ( bilangan bulat )
>>> print(a) # menampilkan variabel a
1153
>>> b = len(Nama) # konversi string dalam variabel nama ke dalam angka
>>> print(b) #menampilkan variabel b
19
>>> type(a) # menampilkan type data variabel a
<class 'int'>
>>> # python menampilkan type data variabel a
>>> type(b) # operasi untuk emenampilkan type data dari variabel b
<class 'int'>
>>> # python menampilkan type data variabel b
>>> a / b # operasi pembagian dari variabel a dan variabel b
60.68421052631579
>>> # python menampilkan hasil dari pembagian variabel a dan variabel b ( 1153 / 19 )
>>> a // b # operasi untuk pembagian dengan pembulatan kebawah dari variabel a dan variabel b
60
>>> # python menampilkan hasi dari pembagian dengan pembulatan dari variabel a dan variabel b ( 1153 // 19 )
>>> 10 * (a - 999) # operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer dengan integer, float dengan float, integer dengan float
1540
>>> # python menampilkan hasil perkalian dari variabel a data type int dengan angka
>>> b ** 2 # operasi ini digunakan untuk perpangkatan
361
>>> # python menampilkan hasil dari perpangkatan b ** 2 ( 19 ** 2 )
>>> a % b # operasi ini digunakan untuk menampilkan sisa hasil bagi
13
>>> #python menampilkan sisa hasil bagi dari variabel a dan variabel b ( 1153 % 19 )
>>> c = 12.5 # variabel c menggunakanangka dengan koma yang berarti type data variabel c adalah float
>>> type(c) # menampilkan type data dari variabel c
<class 'float'>
>>> # python menampilkan type data dari variabel c
>>> a /c # operasi ini di gunakan untuk pembagian
92.24
>>> # python menampilkan hasil pembagian variabel a dan variael c ( 1153 / 12.5 )
>>> a // c # operasi untuk pembagian dengan pembulatan ke bawah
92.0
>>> # python menampilkan hasil pembagian dengan pembulatan kebawah dari variabel a dan c ( 1153 // 12.5 )
>>> a % c # operasi ini digunakan utuk menampilkan sisa hasil bagi
3.0
>>> # python menampilkan sisa hasil bagi dari variabel a dan c ( 1153 % 12.5 )
>>> c > b # operasi ini digunakan untuk menampilkan perbandingan ebih besar dari. type data adalah boolean
False
>>> # python menampilkan hasil perbandingan c > b
>>> type(c > b) # operasi untuk menampilkan type data (c > b)
<class 'bool'>
>>> # python menampilkan hasil perbandingan dari (c > b)
>>> a > b and b > c # pada data terdapat dua pernyataan, kedua pernyataan di hubungkan dengan operator logika "and"
True
>>> #pyton menampilkan hasil dari perbandingan a > b and b > c
>>> a > 1100 or b < 10 # logika yang digunaka adalah "or"
True
>>> # python menampilkan hasil perbandingan dari a > 1100 or b < 10
>>> 
>>> ## Kegiatan 4
>>> Nama ='Anita Lusi Romadhon'
>>> NIM = 153
>>> Tinggi = 1.57
>>> Berat = 54
>>> TaunLahir = 2000
>>> Aku =(TahunLahir, Berat, Tinggi, NIM, Nama)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    Aku =(TahunLahir, Berat, Tinggi, NIM, Nama)
NameError: name 'TahunLahir' is not defined
>>> Aku =(TaunLahir, Berat, Tinggi, NIM, Nama)
>>> Data =[TaunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku) #menampilkan type data variabel aku
<class 'tuple'>
>>> #python menampilkan type data dari variabel Aku
>>> Aku[0] # menampilkan elemen tuple indeks 0
2000
>>> # python menampilkan elemen tuple indeks 0
>>> a = NIM % 4 ; Aku[a] # NIM di bagi 4, lalu sisa hasil bagi dimasukkan ke dalam variabel Aku
54
>>> #python menampilkan hasil dari NIM dibagi 4, sisa hasil bagi 1. lalu indeks 1 dimasukkan ke dalam variabel 1
>>> type(Aku[a]) #menampilkan type data dari elemen tuple indeks a
<class 'int'>
>>> # python menampilkan type data dari elemen tuple indeks a
>>> Aku[a:4] # slicing dimulai dari indeks ke 1 dan akhirnya ke indeks 4
(54, 1.57, 153)
>>> # python menampilkan slicing dari indeks ke 1 dan akhirnya ke indeks 4
>>> type(Aku[4]) # menampilkan type daa dari elemen tuple indeks 4
<class 'str'>
>>> # python menampilkan type data dari elemen tuple indeks 4
>>> Aku[0] = 'ok' # merubah isi dari elemen tuple indeks 0 menjadi ok
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    Aku[0] = 'ok' # merubah isi dari elemen tuple indeks 0 menjadi ok
TypeError: 'tuple' object does not support item assignment
>>> # EROR, karena elemen dalam tuple tidak dapat diubah
>>> type(Data) # menampilkan type data dari variabel Data
<class 'list'>
>>> # python menampilkan type data dari variabel Data
>>> type(Data[4]) # menampilkan data dari elemen list indeks 4
<class 'str'>
>>> # python menampilkan type data dari elemen list indeks 4
>>> Data[4][5] # menampilkan list indeks 5 pada list 4
' '
>>> # python menampilkan list indeks 5 pada list 4
>>> Data[4][a:6] # menampilkan list indeks 1 sampai 5 dari liat 4
'nita '
>>> # python menampilkan list indeks 1 sampai 5 dari list 4
>>> Data[0] = 'ok'; Data # merubah elemen list pada indeks 0 menjadi ok
['ok', 54, 1.57, 153, 'Anita Lusi Romadhon']
>>> #python menampilkan list pada indeks 0 yang diubah menjadi ok
>>> Data[-a] # menampilkan angka/huruf terakhir pada indeks 1 dari list
'Anita Lusi Romadhon'
>>> # python menampilkan angka/huruf dari indeks 1
>>> range(a) # menampilkan semacam daftar atau koleksi dari indeks 1
range(0, 1)
>>> # python menampilkan daftar atau koleksi dari indeks 1
