from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Product, Category, ProductSpec


# Create your views here.

def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            else:
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, id):
    """
    A view to show individual product details
    """

    product = Product.objects.get(id=id)
    sizes = ProductSpec.objects.filter(product=product).values('size__id', 'size__name').distinct()
    papers = ProductSpec.objects.filter(product=product).values('paper__id', 'paper__name', 'price', 'size__id').distinct()

    context = {
        'product': product,
        'sizes': sizes,
        'papers': papers,
    }

    return render(request, 'products/product_detail.html', context)

def add_to_cart(request):
    """ a d """
    del request.session['cartdata']
    cart_p = {}
    cart_p[str(request.GET['id'])] = {
        'name': request.GET['name'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'size': request.GET['size'],
        'paper': request.GET['paper']
    }
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_p[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cartdata'] = cart_data
        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_data)
            request.session['cartdata'] = cart_data
    else:
        request.session['cartdata'] = cart_p
    return JsonResponse({'data': request.session['cartdata']})