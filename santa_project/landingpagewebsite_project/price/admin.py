from django.contrib import admin
from .models import PriceTable, PriceCard


admin.site.register(PriceCard)
admin.site.register(PriceTable)

