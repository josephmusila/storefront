from collections import Counter
import imp
from pyexpat import model
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from store.models import Collection, Customer, Order, OrderItem, Product
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Count


from tags.models import TaggedItem

# Register your models here.

class InventoryFilter(admin.SimpleListFilter):
    title='inventory'
    parameter_name="inventory"

    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
     
        ]

    def queryset(self, request, queryset):
        if self.value()== '<10':
           return queryset.filter(inventory__lt=10)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # inlines=[TagInline]
    autocomplete_fields=['collection']

    prepopulated_fields={
        'slug':['title']
    }
    actions=['clear_inventory']
    list_display=['title','unit_price','inventory_status','collection_title']
    list_editable = ['unit_price']
    list_per_page=10
    list_select_related=['collection']
    list_filter=['collection','last_update',InventoryFilter]

    def collection_title(self,product):
        return product.collection.title


    @admin.action(description="Clear Inventory")
    def clear_inventory(self,request,queryset):
      updated_count=  queryset.update(inventory=0)
      self.message_user(
          request,f'{updated_count} products were succesfully updated.'
      )

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        
        if product.inventory < 10:
           url= reverse('admin:store_product_changelist')
           return format_html('<a href="{}">{}</a>',url,'Low')
           
        return 'Ok'




@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','membership']
    list_editable=['membership']
    ordering=['first_name','last_name']
    # list_per_page=10,
    search_fields=['first_name__istartswith','last_name__istartswith']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    # autocomplete_fields=['featured_product']
    list_display=['title','products_count']
    search_fields=['title']

    def products_count(self,collection):
        return collection.products_count

    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )
class OrderItemInline(admin.StackedInline):
    model=OrderItem
    # autocomplete_fields=['product']
    extra=0
    min_num=1
    max_num=10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]
    autocomplete_fields=['customer']
    list_display=['id','placed_at','customer']
