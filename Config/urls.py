# Config/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home_app import views  # وارد کردن از home_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # صفحه اصلی
    path('contact/submit/', views.contact_submit, name='contact_submit'),  # فرم تماس
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
