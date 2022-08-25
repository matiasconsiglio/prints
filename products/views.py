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

    paper_id = request.GET['paper']
    size_id = request.GET['size']
    product_id = request.GET['id']
    product_qty = int(request.GET['qty'])
    product_spec = ProductSpec.objects.filter(paper__id=paper_id, size__id=size_id, product__id=product_id).first()
    product_spec_id = str(product_spec.id)

    cart = request.session.get('cart', {})
    if product_spec_id in list(cart.keys()):
        cart[product_spec_id] += product_qty
        print("a")
    else:
        cart[product_spec_id] = product_qty
        print("b")
    request.session['cart'] = cart
    final = cart
    print(final)
    print(product_qty)
    
    return JsonResponse({'data': final, 'totalitems':len(request.session['cart'])})
