from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = "Anshuman Admin"
admin.site.site_title = "Portfolio Portal"
admin.site.index_title = "Welcome to Anshuman Portal"

urlpatterns = [
    path('adminanshuman/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout_fun,name='logout_fun'),
    path('about',views.about,name='about'),
    path('computer',views.computer,name='computer'),
    path('contact',views.Contact,name='contact'),
    path('laptop',views.laptop,name='laptop'),
    path('product',views.product,name='product'),
    path('savedata',views.savedata,name='savedata'),
    path('savedata_view',views.savedata_view,name='savedata_view'),

]