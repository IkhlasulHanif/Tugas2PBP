# TUGAS 2
Link heroku : https://pbptugas1hanif.herokuapp.com/

![alt text](https://github.com/IkhlasulHanif/Tugas2PBP/blob/main/images/bagan.png)
1. Saat kita mengunjungi suatu web yang pertama terjadi adalah kita sebagai user meminta request kepada urls.py, selanjutnya urls.py akan memilih views yang sesuai request dari user. Kemudian, pada proses views.py juga menentukan hubungan antara models.py. Terdapat dua kasus, jika views.py memerlukan pertukaran data terhadap database maka transaksi dua arah tersebut dengan perantara yang diatur models.py, sedangkan jika tidak diperlukan pertukaran data maka views.py langsung menentukan page HTML yang tepat pada template. Jika terjadi pertukaran data, maka tidak jauh berbeda dimana views.py akan memilih page HTML yang tepat, tetapi akan menggunakan data melalui models.py. Terakhir HTML yang terpilih akan menampilkan response berupa tampilan web yang diinginkan oleh user.
2. Virtual environment seperti dari namanya membuat suatu lingkungan virtual untuk setiap projek yang kita miliki secara terpisah, dimana suatu environment tersedia hal hal seperti package, libraries yang berbeda tiap environmentnya. Hal ini dilakukan agar tidak terjadi konflik, misal kita sebagai programmer tentu tidak hanya akan melakukan 1 projek saja, terlebih lagi jika projek yang berbeda itu membutuhkan spesifikasi atau lingkungan yang berbeda. Misal projek dari kampus kita membutuhkan django versi 2.3 sedangkan projek pribadi yang kita kerjakan menggunakan django versi terbaru, maka jika menginstallnya secara global bisa jadi akan terjadi error karena bisa jadi terdapat syntax baru yang belum ada di versi 2.3 dan ada syntax yang sudah tidak berlaku lagi pada versi terbaru. Maka, kita perlu virtual environment agar projek kita dapat berjalan sesuai dengan kebutuhan masing masing projek.
3. Langkah-langkah pengerjaan:
   + Melakukan migrasi terlebih dahulu agar dapat web dapat saya cek sebelum dideploy
   + Lalu, saya mengimport Catalogitem dari models.py pada views.py. Pada views.py saya membuat dictionary dengan key item_list (Catalogitem.all(), nama, dan npm yang        nantinya keynya akan dipakai pada templates. Setelah itu kita mereturn request tersebut, dictionary, dan juga page html yang kita inginkan.
   + Kemudian saya menambahkan path fungsi yang telah kita buat sebelumnya pada urs.py (katalog)
   + Saya perlu juga menambahkan path untuk routing pada urls.py di project_django
   + Selanjutnya, saya melakukan sedikit pengaturan pada file html, dimana isi table kita harus melakukan iterasi terhadap item_list yang telah kita definisikan              sebelumnya. Selain itu saya juga melakukan sedikit coba-coba melakukan pengaturan style.
   + Terakhir adalah tahap deployment heroku, yang perlu dilakukan adalah menambahkan secret key yang berupa HEROKU_API_KEY dan HEROKU_APP_NAME yang bisa didapatkan          melalui akun heroku saya. Terakhir dilakukan push atau bisa kita lakukan reattempt push agar web terdeploy secara otomatis.
# TUGAS 3
1. JSON singkatan dari JavaScript Object Notation (bahasa Indonesia: notasi objek JavaScript), adalah suatu format ringkas pertukaran data komputer atau untuk menyimpan dan mentransfer data (data delivery). XML (Extensible Markup Language) adalah bahasa markup yang dibuat oleh World Wide Consortium (W3C) untuk pertukaran dan penyimpanan data yang lebih ringkas, HTML adalah bahasa markup standar yang digunakan untuk membuat halaman website dan aplikasi. Dari sini kita dapat melihat HTML memiliki perbedaan definisi yang cukup jauh, dimana HTML bukan bahasa markup untuk data delivery. Sedangkan perbedaan antara XML dan JSON adalah XML cenderung lebih aman daripada JSON, sedangkan JSON lebih cepat daripada XML. Kemudian JSON dapat menggunakan array dan XML tidak, tapi di XML kita dapat memberikan komen tetapi di JSON tidak.

2. Kita membutuhkan data delivery untuk menghubungkan berbagai framework. Agar kita dapat menghubungkan framework-framework frontend dan backend kita perlu mempunyai suatu cara yang standar untuk menyimpan atau menerima data sehingga aplikasi dapat berjalan dengan baik.

3. Pertama saya membuat app baru dengan nama mywatchlist. Selanjutnya saya membuat urls.py agar dapat routing. Kemudian saya membuat models.py dengan field:
   * watched : TextField
   * title : TextField
   * rating : IntegerField
   * release_date : TextField
   * review : TextField
  
   Setelah itu saya membuat data yang dibutuhkan dalam format JSON. Terakhir saya membuat fungsi pada views.py untuk mengembalikan HTML, XML, dan JSON dan tentunya  menambahkan fungsi views.py ke urls.py pada folder mywatchlist dan juga project-django. Selanjutnya saya melakukan command git agar terdeploy.
  
4. Postman
HTML
![alt text](https://github.com/IkhlasulHanif/Tugas2PBP/blob/main/images/HTML.png)
XML
![alt text](https://github.com/IkhlasulHanif/Tugas2PBP/blob/main/images/XML.png)
JSON
![alt text](https://github.com/IkhlasulHanif/Tugas2PBP/blob/main/images/JSON.png)
 
# TUGAS 4
1. Cross-Site Request Forgery (CSRF) adalah salah satu serangan yang dapat dilakukan pada web dimana penyerang akan mengirimkan permintaan palsu (request forgery) sehingga web tersebut akan mengeksekusi tindakan yang tidak dikehendaki oleh user. Fungsi {% csrf_token %} adalah untuk mengatasi serangan tersebut dengan mengenerate token saat rendering page sehingga web akan melakukan pengecekan terlebih dahulu untuk setiap request yang diberikan. Jika tidak ada potongan kode tersebut maka form akan rawan terhadap serangan CSRF, oleh karena itu browser akan mereject request kita dengan mengirimkan error CSRF token missing.
2. Ya kita dapat membuatnya secara manual langsung di htmlnya, seperti form pada biasanya kita awali dengan elemen </form>. Lalu kita membuat "judul" untuk form tersebut. selanjutnya kita menggunakan tag <input> yang nantinya user dapat memberikan input dan akhirnya dikirim ke database yang dinotifikasi oleh button dengan type=submit.
3. Pertama user mengisi pada form yang tersedia, kemudian saat user mengsubmit data tersebut akan dibawa oleh request ke views.py, selanjutnya kita dapat menggunakan form.save() untuk menyimpan di database atau membuat objek yang kita mau yang akan disimpan di objek dengan Objek.objects.create(), Setelah disimpan di database, maka data dapat dipakai di html dengan bantuan models.py
4. Pertama, kita membuat aplikasi todolist. Selanjutnya, kita membuat routing di urls.py pada django_projects ke todolist.urls. Kemudian, kita membuat class di models.py sesuai dengan spesifikasi soal. Lalu, kita mengimplementasikan login, logout, dan registrasi dengan bantuan method yang disediakan django. Kemudian, kita membuat todolist.html yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task, dimana kita perlu membuat button yang nantinya kita link tombol tersebut dengan link tujuan misal a href="{% url 'todolist:create_task' %}. Setelah itu, kita perlu membuat create_file.html untuk pembuatan task, dimana kita membuat form yang menerima input sesuai spesifikasi di awal, lalu kita juga membuat fungsinya di views.py untuk mengirimkan data yang telah diinput user ke database. Akhirnya kita membuat routing ke fungsi-fungsi yang telah kita buat sebelumnya.
