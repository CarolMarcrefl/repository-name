from django.contrib import admin
from django.urls import path
from companies.views import home  # Ensure you have a view to handle the root path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This line handles the root path
]
