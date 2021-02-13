from django.urls import path
from .views import Register, Login, Dashboard, CreateArticle, Logout, Search
urlpatterns = [
    path('Register', Register, name="Register"),
    path('Login', Login, name="Login"),
    path('Dashboard', Dashboard, name="Dashboard"),
    path('CreateArticle', CreateArticle, name="CreateArticle"),
    path('Search', Search, name="Search"),
    path('Logout', Logout, name="Logout"),
]