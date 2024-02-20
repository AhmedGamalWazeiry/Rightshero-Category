from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from category.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category', index),
    path("api/categories/", include("category.urls")),
    
]+  staticfiles_urlpatterns()

