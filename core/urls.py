from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),            # ← add this line
    path('', include('libraryboxd.urls')),       # ← your app's URLs (hello world, etc.)
]