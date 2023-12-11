from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('insert',views.insertData,name='insertData'),
    path('update/<id>',views.updateData,name='updateData'),
    path('delete/<id>',views.deleteData,name='deleteData'),
    path('confirmDelete/<id>',views.confirmDelete,name='updateData'),
]