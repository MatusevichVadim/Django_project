from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_data', 'coment_text')
    readonly_fields = ('coment_data',)
    extra = 0

class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 10
    list_max_show_all = 100
    fields = (('id', 'order_dt'), 'order_status', ('order_name', 'order_phone'))
    readonly_fields = ('id', 'order_dt')
    #поле класса comment
    inlines = [Coment,]

admin.site.register(Order, AdminOrder)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)

# Register your models here.
