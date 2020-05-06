from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from home.views import home_view
from accounts.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home_view,name='home'),
    url(r'^post/',include('post.urls')),
    url(r'^accounts/',include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)