from django.shortcuts import render
from kiosk.models import Product, Sale
from .forms import SaleForm
from django.forms import formset_factory
from django.utils import timezone

SaleFormSet = formset_factory(SaleForm, extra=0)


def get_products_list(request):
    products_list = Product.objects.all()

    if request.method == 'POST':
        sale_form_set = SaleFormSet(request.POST or None)

        if sale_form_set.is_valid():
            check_time = timezone.now()
            seller = request.user

            for sale_form in sale_form_set:
                quantity = sale_form.cleaned_data.get("quantity")

                if quantity:
                    product = sale_form.cleaned_data.get("product")

                    sale = Sale(product=product, quantity=quantity, seller=seller, check_time=check_time)
                    sale.save()

    else:
        sale_form_set = SaleFormSet(initial=[
            {"product": int(product.id),
             "quantity": 0,
             }
            for product in products_list
        ])

    context = {
        'products_list': products_list,
        'sale_form_set': sale_form_set,
    }

    return render(request, 'kiosk/product_list.html', context)
