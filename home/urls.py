from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
     path("about", views.about, name="about"),
      path("services", views.services, name="services"),
       path("contact", views.contact, name="contact"),
    # Add more paths as needed for your application
]

# Optionally, you can include the admin URLs like this:
# urlpatterns += [path("admin/", admin.site.urls)]
