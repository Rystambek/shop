from django.contrib import admin
from .models import Product,Comment,Like,Order

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Like)