# Bastian Adiputra Siregar
## Tugas 2

[Website](http://bastian-adiputra-regameshop.pbp.cs.ui.ac.id/)
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Membuat sebuah proyek Django baru.

  Buat direktori baru dan masuk ke dalamnya.
  Di dalam direktori yang sama, buat berkas requirements.txt dan tambahkan dependencies berikut.
  ```
  django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
  ```
  
  Buat proyek Django dengan perintah berikut.
  ```
  django-admin startproject <Nama Project> .
  ```

  Tambahkan kedua string berikut pada ALLOWED_HOSTS di settings.py untuk keperluan deployment:
  ```
  ...
  ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
  ...
  ```

  
* Membuat aplikasi dengan nama main pada proyek tersebut.

  Jalankan perintah berikut untuk membuat aplikasi baru dengan nama main.
  ```
  python manage.py startapp main
  ```


* Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

  Tambahkan 'main' ke dalam daftar aplikasi yang ada sebagai elemen paling terakhir. Daftar aplikasi dapat kamu akses pada variabel INSTALLED_APPS.
  ```
  INSTALLED_APPS = [
    ...,
    'main'
  ]
  ```


* Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib

  Modifikasi berkas models.py dengan kode berikut.
  ```
  from django.db import models
  
  class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
  
      def __str__(self):
          return self.name
  ```


* Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

  Memodifikasi views.py yang terletak di dalam berkas aplikasi main.
  ```
  from django.shortcuts import render

  def show_main(request):
      context = {
          'app': 'RegameShop'
          'name': 'Bastian Adiputra Siregar',
          'class': 'PBP D'
      }
  
      return render(request, "main.html", context)
  ```

  Buka berkas main.html yang telah dibuat sebelumnya dalam direktori templates pada direktori main dan modifikasi dengan code berikut.
  ```
  ...
  <h5>NPM: </h5>
  <p>{{ npm }}<p>
  <h5>Name: </h5>
  <p>{{ name }}<p>
  <h5>Class: </h5>
  <p>{{ class }}<p>
  ...
  ```


* Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

  Modifikasi urls.py pada direktori main
  ```
  from django.urls import path
  from main.views import show_main
  
  app_name = 'main'
  
  urlpatterns = [
      path('', show_main, name='show_main'),
  ]
  ```

  Modifikasi urls.py pada direktori proyek
  ```
  from django.contrib import admin
  from django.urls import path,include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('main.urls')),
  ]
  ```


* Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

  Kembali ke settings.py, menambahkan link sesuai format pws
  ```
  # URL deployment PWS memiliki format <username-sso>-<nama proyek>.pbp.cs.ui.ac.id.
  ALLOWED_HOSTS = ["127.0.0.1", "localhost", "<URL LINK>"]
  ```

  jalankan perintah-perintah berikut
  ```
  git remote add origin https://github.com/Bastian2312/regameshop.git
  git remote add pws http://pbp.cs.ui.ac.id/bastian.adiputra/regameshop
  git add .
  git commit -m "Initial commit"
  git branch -M main
  git push -u origin main
  git bracnh -M master
  git push pws master
  ```



### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![alt text](https://cdn.discordapp.com/attachments/817682466965553152/1282744872079458375/image.png?ex=66e078c1&is=66df2741&hm=17a91b7001c97bf72368e7c8f71c3afc579bdcc4fac11e6da448d840d4585e2a&)

Pada aplikasi Django, client request diarahkan oleh urls.py ke views.py yang memproses logika bisnis, mengambil data dari models.py jika diperlukan, lalu merender respon melalui berkas HTML untuk ditampilkan kembali ke client.



### Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah sistem kontrol versi terdistribusi yang digunakan dalam pengembangan perangkat lunak untuk melacak perubahan kode, memungkinkan kolaborasi antar pengembang, mengelola berbagai versi kode, dan memfasilitasi pemulihan jika terjadi kesalahan, sehingga mempermudah pengelolaan proyek secara terorganisir dan efisien.



### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

karena framework ini menawarkan struktur yang jelas dan lengkap, mencakup banyak fitur "out of the box" seperti autentikasi, manajemen database, dan routing URL, sehingga memungkinkan pemula untuk fokus pada logika aplikasi tanpa harus mengatur komponen-komponen dasar dari awal. Django juga menggunakan bahasa pemrograman python yang populer dengan pengguna2 pemula



### Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ini untuk memetakan objek-objek Python (model) ke tabel-tabel dalam database relasional. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan kode Python, tanpa perlu menulis SQL secara langsung. ORM memungkinkan Django untuk mengelola operasi database seperti pembuatan, pembacaan, pembaruan, dan penghapusan data melalui objek-objek Python, sehingga memudahkan manipulasi data dalam aplikasi.


## Tugas 3


###  Membuat input form untuk menambahkan objek model pada app sebelumnya.

* Implementasi Skeleton sebagai Kerangka Views
  Buat direktori templates pada direktori utama (root folder) dan buatlah sebuah berkas HTML baru bernama base.html.
  Isilah berkas base.html tersebut dengan kode berikut:
  ```
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
    </head>
  
    <body>
      {% block content %} {% endblock content %}
    </body>
  </html>
  ```

  Sesuaikan kode dalam settings.py dalam direktori proyek dengan potongan kode berikut
  ```
  ...
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
          'APP_DIRS': True,
          ...
      }
  ]
  ...
  ```

  ubahlah kode berkas main.html menjadi sebagai berikut
  ```
  {% extends 'base.html' %}
  {% block content %}
  <h1>Project Name</h1>
  
  <h5>NPM: </h5>
  <p>{{ npm }}<p>
  
  <h5>Name:</h5>
  <p>{{ name }}</p>
  
  <h5>Class:</h5>
  <p>{{ class }}</p>
  {% endblock content %}
  ```

  Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form
  ```
  from django.forms import ModelForm
  from main.models import ProductEntry
  
  class ProductEntryForm(ModelForm):
      class Meta:
          model = ProductEntry
          fields = ["name","description", "price", "quantity"]
  ```

  dalam views.py dalam direktori main tambahkan beberapa import berikut
  ```
  from django.shortcuts import render, redirect
  from main.forms import ProductEntryForm
  from main.models import ProductEntry
  ```

  buat fungsi baru dengan nama create_product_entry yang menerima parameter request yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form.
  ```
  def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
  ```

  Ubahlah fungsi show_main yang sudah ada pada file views.py
  ```
  def show_main(request):
    mood_entries = ProductEntry.objects.all()

    context = {
        'name': 'Bastian Adiputra Siregar',
        'class': 'PBP D',
        'npm': '2306245005',
        'product_entries':product_entries
    }

    return render(request, "main.html", context)
  ```

  import fungsi create_product_entry dalam file urls.py pada directory main
  ```
  from main.views import show_main, create_product_entry
  ```

  tambahkan path URL ke dalam variabel urlpatterns pada urls.py
  ```
  path('create-product-entry', create_product_entry, name='create-product-entry'),
  ```

  Buat file HTML baru dengan nama create_product_entry.html pada direktori main/templates. Lalu isi dengan kode berikut
  ```
  {% extends 'base.html' %} 
  {% block content %}
  <h1>Add New Product Entry</h1>
  
  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td>
          <input type="submit" value="Add Product" />
        </td>
      </tr>
    </table>
  </form>
  
  {% endblock %}
  ```

  Buka main.html dan tambahkan kode berikut di dalam {% block content %} untuk menampilkan data product
  ```
  {% extends 'base.html' %}
  {% block content %}
  <h1>RegameShop</h1>
  
  <h5>NPM: </h5>
  <p>{{ npm }}<p>
  
  <h5>Name:</h5>
  <p>{{ name }}</p>
  
  <h5>Class:</h5>
  <p>{{ class }}</p>
  
  {% if not product_entries %}
  <p>Belum ada data product pada RegameShop.</p>
  {% else %}
  <table>
    <tr>
      <th>Product Name</th>
      <th>Time</th>
      <th>description</th>
      <th>price</th>
      <th>quantity</th>
    </tr>
  
    {% comment %} Berikut cara memperlihatkan product di bawah baris ini 
    {% endcomment %} 
    {% for product_entry in product_entries %}
    <tr>
      <td>{{product_entry.name}}</td>
      <td>{{product_entry.time}}</td>
      <td>{{product_entry.description}}</td>
      <td>{{product_entry.price}}</td>
      <td>{{product_entry.quantity}}</td>
    </tr>
    {% endfor %}
  </table>
  {% endif %}
  
  <br />
  
  <a href="{% url 'main:create-product-entry' %}">
    <button>Add New Product Entry</button>
  </a>
  {% endblock content %}
  ```
   
