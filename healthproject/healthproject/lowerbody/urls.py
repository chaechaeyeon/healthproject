from django.contrib import admin
from django.urls import path
from lowerbody import views
 
urlpatterns = [
    path('',views.lowerhome,name='lowerbodyHome'),
    path('create/', views.create, name='lowerbodyCreate'),
    path('post_list/',views.post_list, name='lowerbodyList'),
    path('post_detail/<int:id>/',views.post_detail, name='lowerbodyDetail'),
    path('update/<int:id>/',views.post_update, name='lowerbodyUpdate'),
    path('delete/<int:id>', views.post_delete,name='lowerbodyDelete'),    
    path('create_comment/<int:id>', views.create_comment,name='lowerbodyComment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment,name='lowerbodyUpdateComment'),    
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment,name='lowerbodyDeleteComment'),    
]