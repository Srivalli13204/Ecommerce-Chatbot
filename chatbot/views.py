from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

from django.contrib.auth.models import User
from rest_framework import status

from datetime import datetime

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def home(request):
    return render(request, 'chatbot/index.html')

@login_required
def chatbot_view(request):
    return render(request, 'chatbot.html')

# Create your views here.
@api_view(['GET'])
def get_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get('message', '').lower()

    # Extract potential keywords from the message
    keywords = ['headphones', 't-shirt', 'shirt', 'book', 'laptop', 'mobile', 'shoe']
    matched_keyword = next((kw for kw in keywords if kw in user_message), None)

    if not matched_keyword:
        return Response({
            'reply': f"Sorry, I couldn't understand your request.",
            'products': [],
            'timestamp': datetime.now()
        })

    products = Product.objects.filter(name__icontains=matched_keyword)
    serializer = ProductSerializer(products, many=True)

    if products.exists():
        reply = f"Found {products.count()} product(s) matching '{matched_keyword}'."
    else:
        reply = f"Sorry, no products found for '{matched_keyword}'."

    return Response({
        'reply': reply,
        'timestamp': datetime.now(),
        'products': serializer.data
    })