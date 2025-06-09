from django.urls import path
from .views import get_products
from .views import register_user
from .views import chatbot_response
from .views import home, chatbot_view

urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('register/', register_user),
    path('api/chat/', chatbot_response),
    path('', home, name='home'),
    path('chatbot/', chatbot_view, name='chatbot'),
]