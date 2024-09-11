from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name= 'home'),
    path('logout', views.logout_user, name ='logout'),
    path('addBook', views.addBook, name= 'addBook'),
    path('adminhome', views.adminhome, name= 'adminhome'),
    path('adminn', views.admin, name= 'adminn'),
    path('borrow', views.borrow, name= 'borrow'),
    path('period', views.period, name= 'period'),
    path('profile', views.profile, name= 'profile'),
    path('showbooks', views.showbooks, name= 'showbooks'),
    path('signup', views.signup, name= 'signup'),
    path('studentsignup', views.studentsignup, name= 'studentsignup'),
    path('adminsignup', views.adminsignup, name= 'adminsignup'),
    path('updateform', views.updateform, name= 'updateform'),
    path('<int:id>', views.updateBook, name= 'updateBook'),
    path('search', views.search, name= 'search'),
]
