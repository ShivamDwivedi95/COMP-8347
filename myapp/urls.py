from django.urls import path
from django.urls import include
from .import views
app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/',views.about, name='about'),
    path(r'courses/', views.courses, name='courses'),
    path(r'place_order/', views.place_order, name='place_order'),
    path(r'courses/<int:cour_id>', views.coursedetail),
    path(r'<int:top_no>', views.detail, name='detail'),
]