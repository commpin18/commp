from django.urls import path
from . import views


app_name = 'flashcard'
urlpatterns= [
    # resources link
    path('', views.index, name='index'),


    # detail view
    path('<int:pk>/',views.ContentDetail.as_view(), name='detail'),


    # to display article items
    path('video/<int:id>', views.video, name='play_image'),


    # to bookmark
    path('favourite/<int:id>', views.favourite_posts, name='favourite_posts'), 
    path('favourites/', views.posts_favourite_list, name='posts_favourite_list'),

    # to comment
    path('<int:id>/comment', views.AddCommentView.as_view(), name='add_comment'),
    


    

    
   

]
