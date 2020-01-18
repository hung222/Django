# Django

## Cài đặt
### Trên Windows 
+ Cài Python 3.7
+ `pip install django`
+ Tạo project với thư mục admin: `django-admin startproject mywebsite .`
## Tạo ứng dụng:
+ `python manage.py startapp home`
+ Khai báo ứng dụng home cho project tại file settings.py:
  
  ```py
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home'
  ]
  ```
 
 + Cập nhật project: `python manage.py migrate`
 + Viết chương trình đầu tiên:
    + Trong file views.py:
    
    ```py
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(response):
        response = HttpResponse()
        response.writelines("<h1>Xin chào</h1>")
        response.write("<h2>Đây là app home</h2>")
        return response
    ```
    
    + Trong file urls.py:
    
    ```py
      from django.urls import path
      from . import views

      urlpatterns = [
        path('', views.index)
      ]
    ```
    
    + Trong file tests.py:
    
    ```py
    from django.test import TestCase, SimpleTestCase
    class SimpleTest(SimpleTestCase)
      def test_home_status(self)
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)
    ```
    
    + Trong file mywebsite/urls.py 
    
    ```py
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
      path('admin/', admin.site.urls),
      path('home/', include('home.urls'))
    ]
    ```
   
