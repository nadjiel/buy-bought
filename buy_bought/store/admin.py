from django.contrib import admin
from .models import Product

# Allow admins to manage products through
# the default administrative module interface.
admin.site.register(Product)
