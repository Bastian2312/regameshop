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
  ```py
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
  ```py
  INSTALLED_APPS = [
    ...,
    'main'
  ]
  ```


* Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib

  Modifikasi berkas models.py dengan kode berikut.
  ```py
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
  ```py
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
  ```html
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
  ```py
  from django.urls import path
  from main.views import show_main
  
  app_name = 'main'
  
  urlpatterns = [
      path('', show_main, name='show_main'),
  ]
  ```

  Modifikasi urls.py pada direktori proyek
  ```py
  from django.contrib import admin
  from django.urls import path,include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('main.urls')),
  ]
  ```


* Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

  Kembali ke settings.py, menambahkan link sesuai format pws
  ```py
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
  ```html
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
  ```py
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
  ```html
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
  ```py
  from django.forms import ModelForm
  from main.models import ProductEntry
  
  class ProductEntryForm(ModelForm):
      class Meta:
          model = ProductEntry
          fields = ["name","description", "price", "quantity"]
  ```



* Mengubah Primary Key Dari Integer Menjadi UUID
  Tambahkan baris ini pada berkas models.py di subdirektori main/.
  ```py
  import uuid

  class ProductEntry(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      name = models.CharField(max_length=255)
      description = models.TextField()
      price = models.IntegerField()
      quantity = models.IntegerField()
  ```

  Lakukan migrasi model dengan menjalankan perintah berikut.
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```


  
* Membuat Form Input Data dan Menampilkan Data Product Entry Pada HTML
  dalam views.py dalam direktori main tambahkan beberapa import berikut
  ```py
  from django.shortcuts import render, redirect
  from main.forms import ProductEntryForm
  from main.models import ProductEntry
  ```

  buat fungsi baru dengan nama create_product_entry yang menerima parameter request yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form.
  ```py
  def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
  ```

  Ubahlah fungsi show_main yang sudah ada pada file views.py
  ```py
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
  ```py
  from main.views import show_main, create_product_entry
  ```

  tambahkan path URL ke dalam variabel urlpatterns pada urls.py
  ```py
  path('create-product-entry', create_product_entry, name='create-product-entry'),
  ```

  Buat file HTML baru dengan nama create_product_entry.html pada direktori main/templates. Lalu isi dengan kode berikut
  ```html
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
  ```html
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
   


### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

* Mengembalikan Data dalam Bentuk XML, JSON
  tambahkan import HttpResponse dan Serializer dalam views.py pada directory main
  ```py
  from django.http import HttpResponse
  from django.core import serializers
  ```

  Buatlah sebuah fungsi baru yang menerima parameter request dengan nama show_xml, show_json dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada ProductEntry. Lalu tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML/Json dan parameter content_type="application/xml" dan content_type="application/json".
  ```py
  def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")'

  def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```


* Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
  Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml"/"application/json". Pada dalamnya buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada ProductEntry.
  ```py
  def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

  def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```



### Membuat routing URL untuk masing-masing views yang telah ditambahkan

  Buka urls.py yang ada pada direktori main dan import fungsi yang sudah kamu buat tadi.
  ```py
  from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
  ```

  Tambahkan path URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
  ```py
  path('xml/', show_xml, name='show_xml'),
  path('json/', show_json, name='show_json'),
  path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
  path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
  ```

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery merupakan key element yang memungkinkan interaksi antar komponen dalam sebuah platform. Fungsi utamanya adalah memastikan bahwa aliran data antara server dan klien berjalan dengan efisien. Dalam konteks ini, data delivery berperan sebagai jembatan penghubung yang memfasilitasi komunikasi, pertukaran informasi, serta sinkronisasi proses, sehingga sistem dapat berfungsi secara optimal.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON memiliki struktur yang lebih sederhana dan lebih mudah dibaca, baik oleh manusia maupun PC. JSON menggunakan format berbasis objek dengan key-value pairs yang secara intuitif lebih mudah dipahami.

XML, meskipun fleksibel dan kaya fitur, memiliki sintaks yang lebih verbose dengan tag pembuka dan penutup, yang bisa membuat dokumen menjadi lebih panjang dan lebih sulit dibaca.

Menurut saya antara XML dan JSON, JSON lebih unggul karena alsan tersebut yaitu JSON lebih simple dan felksibal dan XML lebih complex dan tidak se-fleksibel JSON. Karena alasa ini juga mengapa JSON lebih populer dari XML

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form di Django digunakan untuk memeriksa apakah data yang dikirimkan ke form sesuai dengan aturan validasi yang telah didefinisikan. Metode ini penting karena membantu kita memastikan bahwa data yang diterima aplikasi sesuai dengan format dan aturan yang benar sebelum diproses lebih lanjut.

### Mengakses keempat URL menggunakan Postman
* XML
  ![xml](https://cdn.discordapp.com/attachments/817682466965553152/1285573577311129701/image.png?ex=66eac331&is=66e971b1&hm=60468b49f3b57422ec604c8a1c860124f708b2ca2f0033caef65ebacfb02313c&)

* JSON
  ![json](https://cdn.discordapp.com/attachments/817682466965553152/1285619660636815474/image.png?ex=66eaee1c&is=66e99c9c&hm=29b9685cd06a8b86cc7a7158d695afabe1bb8ded1090e74a347ea9b2a2ae186a&)

* XML by ID
  ![xml by id](https://cdn.discordapp.com/attachments/817682466965553152/1285619805386444821/image.png?ex=66eaee3f&is=66e99cbf&hm=43411d351276e558a96150487e75b10bdb97a34c9727a747a0f7334b9260ccdd&)

* JSON by ID
  ![json by id](https://cdn.discordapp.com/attachments/817682466965553152/1285573813450309743/image.png?ex=66eac369&is=66e971e9&hm=95974075f181a4019cbaea4c67c3ba5a9c4c0cb00f76b0c0ce393898bc433459&)


## Tugas 4


### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Pada views.py dalam subdirektori main, tambahkan imports berikut

```py
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
```

Tambahkan method login, logout, register pada views.py

login
```py
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():    # Ambil user, lalu login sebagai user
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now())) # Set cookie last_login
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

logout
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

register
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():    # Menyimpan data dari form jika valid
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Update show_main dan create_product_entry dengan code berikut

show_main
```py
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)    # Filter sesuai user yang memberi request

    context = {
        'app' : 'Chicken-Daddy',
        'name': request.user.username,    # Menunjukkan username user yang membuat request pada field name
        'class': 'PBP D',
        'products': product_entries,
        'last_login': request.COOKIES['last_login'],    # Menunjukkan last_login yang diambil dari cookie
    }

    return render(request, "main.html", context)
```

create_product_entry
```py
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)    # mendapatkan model
        product_entry.user = request.user    # menambahkan data terhadap model tersebut
        product_entry.save()    # menyimpan model
        return redirect('main:show_main')
    
    context = {'form' : form}
    return render(request, "create_product_entry.html", context)
```

Dalam folder templates pada folder main, buatlah fuile login.html & register.html

login.html
```html
<!-- login.html -->
{% extends 'base.html' %}
{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

register.html
```py
<!-- register.html -->
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```


### Menghubungkan model Product dengan User.

Update models.py dengan code berikut
```py
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Menambah line ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
```

buatlah minimal 1 akun terlebuh dahulu, lalu lakukan migration
```
python manage.py makemigrations
python manage.py migrate
```

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

![alt text](https://cdn.discordapp.com/attachments/817682466965553152/1288155565729775627/image.png?ex=66f427db&is=66f2d65b&hm=237f0d0f9bf0231847982a44cc183e38322d7eca495e6bdf83706874008b71e1&)

### Apa perbedaan antara HttpResponseRedirect() dan redirect()
Dalam kasus HttpResponseRedirect argumen pertama hanya dapat berupa url, sedangkan redirect pada akhirnya akan mengembalikan HttpResponseRedirect tetapi dapat menerima model, view, atau url sebagai argumen. Sehingga, redirect() lebih fleksibel dalam hal apa yang bisa "dialihkan".

### Jelaskan cara kerja penghubungan model Product dengan User!

Authentication merupakan proses untuk memverifikasi identitas pengguna, sedangkan Authorization adalah proses untuk memverifikasi hak akses pengguna. Dalam Django, kedua konsep ini diimplementasikan dengan cara yang berbeda. Otentikasi di Django dilakukan melalui model User dan metode bawaan seperti login, logout, dan authenticate. Sementara itu, otorisasi di Django diterapkan menggunakan decorators seperti login_required(), yang berfungsi untuk membatasi akses hanya bagi pengguna yang telah di authenticate.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan sessions dan cookies. Saat pengguna berhasil login, Django membuat sesi yang menyimpan informasi pengguna, seperti ID pengguna, di server. Setiap sesi diidentifikasi dengan ID sesi yang unik. Django kemudian mengirimkan cookie ke browser pengguna yang berisi ID sesi tersebut. Cookie ini akan dikirimkan kembali ke server dengan setiap permintaan yang dilakukan oleh pengguna, memungkinkan Django untuk mengenali pengguna yang sama dan menjaga status login mereka.

Cookies juga memiliki berbagai kegunaan lainnya, seperti menyimpan preferensi pengguna atau menyimpan informasi tentang barang-barang yang ditambahkan ke cart belanja dalam aplikasi e-commerce. Namun, tidak semua cookies aman digunakan. Ada beberapa pertimbangan terkait keamanan cookies, seperti perbedaan antara cookies sesi dan cookies persisten, risiko pencurian cookies jika tidak dilindungi dengan baik, serta pentingnya menggunakan atribut SameSite untuk melindungi dari serangan CSRF.
