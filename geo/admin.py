from django.contrib import admin

# Register your models here.
from geo.models import Hornet,HornetNode

class HornetAdmin(admin.ModelAdmin):
    fields = ('lat', 'lng','email','view_dtime',)
    list_display = ('id','view_dtime','lat', 'lng','email',)

admin.site.register(Hornet,HornetAdmin)
admin.site.register(HornetNode)


