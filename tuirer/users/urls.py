from django.urls import path
from users.views import ProfileView, ProfileEditView, UserLoginView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name='profile-edit'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('login/', UserLogoutView.as_view(), name='logout'),
]