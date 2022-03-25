from django.test import TestCase
from django.http import HttpResponse
# Create your tests here.


def product_list(request):
    return  HttpResponse('ok')