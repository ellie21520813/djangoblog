from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('product/', include('product.urls')),
    path('contact/', include('contact.urls')),
    path('usermem/', include('usermem.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)