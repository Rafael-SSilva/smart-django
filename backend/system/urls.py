
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls'), name='account'),
    path('', include('chargesession.urls'), name='chargesession'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
