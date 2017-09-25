from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.

# Load Customer Model
from .models import Customer 

# Create CustomerAdmin Class to view admin page
class CustomerAdmin(admin.ModelAdmin):
  exclude = (
  'cus_cmf_1', 
  'cus_cmf_2', 
  'cus_cmf_3', 
  'cus_cmf_4', 
  'cus_cmf_5', 
  'cus_cmf_6', 
  'cus_cmf_7', 
  'cus_cmf_8', 
  'cus_cmf_9', 
  'cus_cmf_10',)
  list_display = ('customer_id', 'customer_name', 'owner', 'create_user', 'create_time', 'update_user', 'update_time')
  

# register CustomerAdimin clasee on admin page
admin.site.register(Customer, CustomerAdmin)