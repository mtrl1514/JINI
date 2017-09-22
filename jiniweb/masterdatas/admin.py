from django.contrib import admin

# Register your models here.

# Load Customer Model
from .models import Customer 

# Create CustomerAdmin Class to view admin page
class CustomerAdmin(admin.ModelAdmin):
  list_display = ('customer_id', 'customer_name', 'owner', 'create_user', 'create_time', 'update_user', 'update_time')

# register CustomerAdimin clasee on admin page
admin.site.register(Customer, CustomerAdmin)