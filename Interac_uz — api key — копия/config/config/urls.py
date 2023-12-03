
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('interactadmin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('', include('interact_uz.urls'))
]
