from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from kiosk.models import Product, Sale
from .forms import ProductsListForm, SaleForm
from django.core.serializers import deserialize
from django.forms import formset_factory

SaleFormSet = formset_factory(SaleForm, extra=0)


def index(request):
    return HttpResponse("Hello, it's Zelen Kiosk project!")


# class ListProductView(ListView):

#    model = Product
#    template_name = 'kiosk/product_list.html'


def get_products_list(request):
    sale_form_set = []

    products_list = Product.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductsListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print([i for i in deserialize("json", form.__getitem__("products_list"))])

    # if a GET (or any other method) we'll create a blank form
    else:
        # form = ProductsListForm()
        sale_form_set = SaleFormSet(initial=[
            {"product": int(product.id)} for product in products_list
        ])

    return render(request, 'kiosk/product_list.html', {'sale_form_set': sale_form_set, 'products_list': products_list})
