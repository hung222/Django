# Django

## Cài đặt
### Trên Windows 
+ Cài Python 3.7
+ `pip install django`
+ Tạo project đầu tiên: `django-admin startproject mywebsite .`
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
 + Viết chương trình ứng dụng home đầu tiên:
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
    
    ## Tạo template:
    Mục đích tạo template trong Django là để tái sử dụng giao diện nhiều lần trong project và ứng dụng
    
    Trong thư mục home tạo:
    + templates/pages/base.html: Ý ở đây là template nền tảng
    
      ```html
      <!DOCTYPE html>
      <html>
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <meta http-equiv="X-UA-Compatible" content="ie=edge">
              <title>{% block title%} {% endblock %}</title>
          </head>
          <body>
          Content:

          {% block content %}
          {% endblock %}
          </body>
      </html>
      ```
+ templates/pages/home.html: Ở đây, home.html được kế thừa từ template base.html:

  ```html
    {% extends "pages/base.html" %}

    {% block title %}Home{% endblock %}

    {% block content %} 
        <h1>Xin chào</h1>
        <h2>Đây là app home</h2>
    {% endblock %}
  ```
+ File views.py viết:

  ```py
  from django.shortcuts import render
  from django.http import HttpResponse
  
  def index(request):
    return render(request, 'pages/home.html')
  ```
  
+ Chạy project: `python manage.py runserver`
   
