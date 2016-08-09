from django.contrib import admin
from .models import Restaurant, Category, City, Establishment, Payment, Tip

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Establishment)
admin.site.register(Payment)
admin.site.register(Tip)
