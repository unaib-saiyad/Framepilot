from django.urls import path
from . import views
app_name = 'my_app'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('group_by_owners/', views.group_by_owners, name='group_by_owners'),
    path('quadratic_equation/', views.QuadraticRoots.as_view(), name='quadratic_equation'),
]

