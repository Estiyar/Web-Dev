import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

Category.objects.all().delete()
Product.objects.all().delete()

electronics = Category.objects.create(name='Electronics')
clothing = Category.objects.create(name='Clothing')
books = Category.objects.create(name='Books')
sports = Category.objects.create(name='Sports')

products = [
    ('iPhone 15', 999.99, 'Apple smartphone', 10, electronics),
    ('Samsung TV 55"', 799.99, 'Smart TV 4K', 5, electronics),
    ('Laptop Dell', 1200.00, 'Dell Inspiron 15', 8, electronics),
    ('AirPods Pro', 249.99, 'Wireless earbuds', 20, electronics),
    ('iPad Air', 599.99, 'Apple tablet', 12, electronics),
    ('Nike T-Shirt', 29.99, 'Cotton t-shirt', 50, clothing),
    ('Adidas Hoodie', 59.99, 'Warm hoodie', 30, clothing),
    ('Levi\'s Jeans', 79.99, 'Classic jeans', 40, clothing),
    ('Puma Sneakers', 89.99, 'Running shoes', 25, clothing),
    ('Zara Jacket', 119.99, 'Winter jacket', 15, clothing),
    ('Python Crash Course', 39.99, 'Learn Python fast', 100, books),
    ('Clean Code', 44.99, 'Write better code', 80, books),
    ('The Pragmatic Programmer', 49.99, 'Programming best practices', 60, books),
    ('Django for Beginners', 34.99, 'Build web apps', 70, books),
    ('JavaScript: The Good Parts', 29.99, 'JS fundamentals', 90, books),
    ('Football', 24.99, 'Size 5 football', 200, sports),
    ('Tennis Racket', 89.99, 'Professional racket', 45, sports),
    ('Yoga Mat', 19.99, 'Non-slip mat', 150, sports),
    ('Dumbbells 10kg', 34.99, 'Set of 2', 60, sports),
    ('Cycling Helmet', 49.99, 'Safety helmet', 35, sports),
]

for name, price, description, count, category in products:
    Product.objects.create(
        name=name,
        price=price,
        description=description,
        count=count,
        is_active=True,
        category=category
    )

print('Done! Created 4 categories and 20 products.')
