from django.urls import path
from user_form.views import UserFormAPIView

urlpatterns = [
    path('user-form/', UserFormAPIView.as_view(), name='user-form'),
]
