import imp
from turtle import title
from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Collection, Customer, Order, Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F,Func,ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg,Sum
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction
from django.db import connection
# Create your views here.

# @transaction.atomic()
def sayHello(request):

    # queryset=Product.objects.filter(unit_price__range=(20,30))
    # queryset=Product.objects.filter(collection__id__range=(1,2,3))
    # queryset=Product.objects.filter(title__icontains='coffee')
    # queryset=Product.objects.filter(last_update__year=2021)
    # queryset=Product.objects.filter(description_isNull=True)
    # queryset=Product.objects.filter(inventory=F('unit_price'))
    # queryset=Product.objects.order_by('unit_price','-title').reverse()
    # queryset=Product.objects.order_by('unit_price')[0]
    # queryset=Product.objects.earliest('unit_price')
    # queryset=Product.objects.latest('unit_price')
    # queryset=Product.objects.all()[:5]
    # queryset=Product.objects.values('id','title','collection__title')
    # queryset=Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    # queryset=Product.objects.select_related('collection').all()
    # queryset=Product.objects.prefetch_related('collection')

    # queryset=Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # result=Product.objects.filter(collection_id=1).aggregate(count=Count('id'),min_price=Min('unit_price'))
    
    # queryset=Customer.objects.annotate(is_new=Value(True))
    # queryset=Customer.objects.annotate(new_id=F('id')+1)

    # queryset=Customer.objects.annotate(
    #     full_name=Func(F('first_name'),Value(" "),F('last_name'),function='CONCAT')
    # )
    # queryset=Customer.objects.annotate(
    #     full_name=Concat('first_name',Value(' '),'last_name')
    # )

    # queryset=Customer.objects.annotate(
    #     orders_count=Count('order')
    # )
    # discounted_price=ExpressionWrapper(F('unit_price') * 0.8,output_field=DecimalField())
    # queryset=Product.objects.annotate(
    #    discounted_price=discounted_price
    # )

    # content_type = ContentType.objects.get_for_model(Product)


    # queryset=TaggedItem.objects. select_related('tag').filter(
    #     content_type=content_type,
    #     object_id=1
    # )

    # TaggedItem.objects.get_tags_for(Product,1)
    queryset= Product.objects.all()

    collection=Collection(pk=11)
    # collection.title="games"
    # # collection.featured_product=Product(pk=1)
    # collection.featured_product=None
    # collection.save()

    # Collection.objects.filter(pk=11).update(featured_product=None)

    # collection.delete()

    # Collection.objects.filter(id__gt=5).delete()
    # with transaction.atomic():
    #     order=Order()
    #     order.customer_id=1
    #     order.save()

    #     item=OrderItem()
    #     item.order=order
    #     item.product_id=-1
    #     item.quantity=1
    #     item.unit_price=10
    #     item.save()

    # queryset=Product.objects.raw('SELECT * FROM store_product')
    with connection.cursor() as cursor:
        # cursor=connection.cursor()
        cursor.execute('')
        # cursor.close()

    

    
    return render(request,"hello.html",{'result':list(queryset)})