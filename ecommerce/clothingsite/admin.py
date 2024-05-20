from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate,Size
 
# Register your models here.

admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'subcategory', 'product_name', 'category')
admin.site.register(Product,ProductAdmin)

# class ProductAttributeAdmin(admin.ModelAdmin):
#     list_display=('product', 'size')
# admin.site.register(ProductAttribute,ProductAttributeAdmin)