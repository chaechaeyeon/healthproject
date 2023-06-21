from django.contrib import admin
from django.urls import path
from upperbody import views

urlpatterns = [
    path('',views.upperhome,name='upperbodyHome'),
    path('create/', views.create, name='upperbodycreate'),
    path('post_list/',views.post_list, name='upperbodyList'),
    path('post_detail/<int:id>/',views.post_detail, name='upperbodyDetail'),
    path('update/<int:id>/',views.post_update, name='upperbodyUpdate'),
    path('delete/<int:id>', views.post_delete,name='upperbodyDelete'),    
    path('create_comment/<int:id>', views.create_comment,name='upperbodyComment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment,name='upperbodyUpdateComment'),    
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment,name='upperbodyDeleteComment'),    
]