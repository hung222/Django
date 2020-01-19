from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls'))
]
handler400 = 'home.views.error404'
handler500 = 'home.views.error500'