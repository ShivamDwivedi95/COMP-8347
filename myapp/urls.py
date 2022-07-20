from django.urls import path
from django.urls import include
from .import views
app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about),
    path(r'courses/', views.courses),
    path(r'place_order/', views.place_order),
    path(r'login/', views.user_login),
    path(r'logout/', views.user_logout),
    path(r'myaccount/', views.myaccount),

    path(r'courses/<int:cour_id>', views.coursedetail),
    path(r'<int:top_no>/', views.detail),

    # path(r'myaccount/', views.myaccount, name='myaccount')
]