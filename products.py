import os
import django
import random

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_bot.settings")
django.setup()

from chatbot.models import Product

# Clear old data
Product.objects.all().delete()

# Mock data pool
names = ["T-Shirt", "Headphones", "Notebook", "Jeans", "Sneakers", "Backpack", "Smartphone", "Jacket", "Sunglasses", "Watch"]
categories = ["Clothing", "Electronics", "Books", "Accessories", "Footwear"]
descriptions = [
    "High-quality and comfortable",
    "Latest model with advanced features",
    "Perfect for daily use",
    "Trendy and durable",
    "Lightweight and stylish"
]
images = [
    "https://via.placeholder.com/150",
    "https://placekitten.com/150/150",
    "https://placebear.com/150/150",
]

# Generate 100 mock products
for i in range(100):
    name = random.choice(names) + f" #{i+1}"
    category = random.choice(categories)
    price = round(random.uniform(10, 999), 2)
    rating = round(random.uniform(1, 5), 1)
    description = random.choice(descriptions)
    image_url = random.choice(images)

    Product.objects.create(
        name=name,
        category=category,
        price=price,
        rating=rating,
        description=description,
        image_url=image_url,
    )

print("✅ 100 products loaded.")