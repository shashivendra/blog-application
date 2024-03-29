from django.urls import path
from .import views

urlpatterns = [
    
    # path('', views.home, name="home"),
    # path('savequiry/', views.savequiry, name='add_category'),
    path('', views.Welcome, name='welcome'),
    path('sign-up', views.SignUp_Form, name='sign_up'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutView, name ='logout_view'),
    path('add-blog', views.addblog, name='add_blog'),
    path('post-list/',views.post_list, name ='post_list'),
    path('post-detail/<int:post_detail_id>/', views.post_detail, name ='post_detail'),
    path('author-name', views.author_name, name = 'add_name'),
    path('comment/' ,views.blog_comment, name ='add_comment'),
     
    ]
     


