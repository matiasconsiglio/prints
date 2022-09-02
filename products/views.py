from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.db.models.functions import Lower
from .models import Product, Category, ProductSpec
from .forms import ProductForm, SpecForm


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
    # del request.session['bag']
    paper_id = request.GET['paper-id']
    size_id = request.GET['size-id']
    product_id = request.GET['id']
    product_qty = int(request.GET['qty'])
    product_price = request.GET['price']
    product_name = request.GET['name']
    product_size = request.GET['size']
    product_paper = request.GET['paper']
    product_spec = ProductSpec.objects.filter(paper__id=paper_id, size__id=size_id, product__id=product_id).first()
    product_spec_id = str(product_spec.id)
    cart_data = {}

    cart_data[product_spec_id] = {
        'qty': product_qty,
        'price': product_price,
        'name': product_name,
        'size': product_size,
        'paper': product_paper
    }
    bag = request.session.get('bag', {})

    if product_spec_id in list(bag.keys()):

        bag[product_spec_id]['qty']+=product_qty
        messages.success(request, f'Added {product_name} with: {product_paper} paper type and {product_size} size to your bag')

    else:
        bag.update(cart_data)
        messages.success(request, f'Added {product_name} to your bag')

    request.session['bag'] = bag
    
    return JsonResponse({'data': bag})

def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def add_product_spec(request):
    """ Add a product to the store """
    form = SpecForm()
    template = 'products/add_product_spec.html'
    context = {
        'form': form,
    }

    return render(request, template, context)