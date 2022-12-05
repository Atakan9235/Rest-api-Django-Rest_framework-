# Rest-api-Django-Rest_framework-

Django  altyapısı kullanılarak Rest framework kütüphanesi ile temel bir restapi oluştrulmuştur.Veritabanına Id,ad,soyad bilgisi işlenmiştir.Yeni bir veri eklemek değiştirmek içi views fonksiyonları yazılmıştır.Proje python manage.py runserver ile çalıştırlacaktır.Veriler http://127.0.0.1:8000/ linki ile izlenebilir.

http://127.0.0.1:8000/add ile yeni veri gönderimi aşağıdaki formattaki şekilde gönderilebilir.
#
{
  "id": 4
  "Ad": "Namık",
  "Soyad": "Kemal"
}

http://127.0.0.1:8000/1 linki /1 id numarasını temsil etme koşulu ile veri değiştirilebilir veya tamamen silinebilir.
