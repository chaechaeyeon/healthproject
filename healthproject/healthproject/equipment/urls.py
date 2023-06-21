from django.contrib import admin
from django.urls import path
from equipment import views

urlpatterns = [
    path('',views.equipmenthome,name='equipmentHome'),
    path('create/',views.create,name='equipmentCreate'),
    path('post_list/',views.post_list, name='equipmentList'),
    path('post_detail/<int:id>/',views.post_detail, name='equipmentDetail'),
    path('update/<int:id>/',views.post_update, name='equipmentUpdate'),
    path('delete/<int:id>', views.post_delete,name='equipmentDelete'),
    path('create_comment/<int:id>', views.create_comment,name='equipmentComment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment,name='equipmentUpdateComment'),    
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment,name='equipmentDeleteComment'),    

]
