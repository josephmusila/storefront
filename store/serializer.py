
from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection, Reviews

class CollectionSerializer(serializers.ModelSerializer):
   class Meta:
       model=Collection
       fields=['id','title','products_count']


   products_count=serializers.ImageField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)
    # price=serializers.DecimalField(max_digits=6,decimal_places=2,source='unit_price')
    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    collection=serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    collection=serializers.StringRelatedField()
    # collection=CollectionSerializer()
    # # collection = serializers.HyperlinkedRelatedField(queryset=Collection.objects.all(),view_name='collection-detail')

    def calculate_tax(self,product:Product):
        return product.unit_price *  Decimal(1.1) 

    class Meta:
        model= Product
        fields=['id','title','description','unit_price', 'slug', 'inventory', 'price_with_tax','collection']

    # def validate(self, data):
    #     return super().validate(attrs)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=['id','date','name','description','product']

        