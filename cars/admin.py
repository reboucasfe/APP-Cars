from cars.models import Car
from django.contrib import admin

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value')
    search_fields = ('model',)
    
admin.site.register(Car, CarAdmin)


