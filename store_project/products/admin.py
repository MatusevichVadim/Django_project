from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', ('short_description', 'description'), ('price', 'quantity'), 'category')
    readonly_fields = ('quantity',)
    ordering = ('name',) #сортировка
    search_fields = ('name',)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp', )
    extra = 0 #в админке у пользователя сделать пустым поле корзины
