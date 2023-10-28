from django.contrib import admin
from django.urls import path
                            module views
from modelo import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('page/',v.page1, nome='page1'),
    path('page/delete/<id:int>', v.delete, nome='delete')
]