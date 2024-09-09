# Bastian Adiputra Siregar
## Tugas 2

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
