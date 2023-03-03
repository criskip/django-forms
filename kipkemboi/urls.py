"""kipkemboi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from  django.contrib import admin
from . import views
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regpage/', views.reg, name='regpage'),
    path('people/', views.reg_people, name = 'people'),
    path('students/', views.reg_students, name = 'students'),
    path('', view.index_page, name = 'index'),
    path('', view.edit_page, name = 'edit'),
    path('', view.login_page, name = 'login'),
    path('', view.signup_page, name = 'signup'),
    path('insert', view.insertData, name = 'insertdata'),
    path('delete/<id>', view.deleteData, name = 'deleteData'),
    path('update/<id>', view.updateData, name = 'updateData')
]
