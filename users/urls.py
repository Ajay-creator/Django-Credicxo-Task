from django.urls import path
from .views import StudentAddView, LoginView, UserView, LogoutView, StudentListView

urlpatterns = [
    path('register/', StudentAddView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('listStudents/', StudentListView.as_view()),
]
