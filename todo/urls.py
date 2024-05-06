from django.urls import path
from .views import home,singup,login,logout,completed,deleted,edited_mode,update_todo
urlpatterns = [
    path("",home,name="dashboard"),
    path("completed/<int:id>",completed,name="completed"),
    path("deleted/<int:id>",deleted,name="deleted"),
    path("edit/<int:id>",edited_mode,name="edit"),
    path("update/<int:id>", update_todo, name="update_todo"),
    path("register/",singup,name="register"),
    path("login/",login,name="login"),
    path('logout/',logout,name="logout"),
]
