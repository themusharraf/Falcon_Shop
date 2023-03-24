from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.urls'))

  ] + static(STATIC_URL,document_root=STATIC_ROOT) + static(MEDIA_URL,document_root=MEDIA_ROOT)
