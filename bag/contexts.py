from decimal import Decimal
from django.conf import settings
from products.models import Product, ProductSpec

def bag_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    qty_per_product = 0
    price = 0
    total_per_product = 0
    name = ''
    size = ''
    paper = ''
    product_spec_id = 0

    bag = request.session.get('bag', {})

    for product_spec_id in bag.keys():
        
        product_id = product_spec_id
        name = bag[product_spec_id]['name']
        size = bag[product_spec_id]['size']
        paper = bag[product_spec_id]['paper']
        price = int(bag[product_spec_id]['price']) 
        total_per_product += (bag[product_spec_id]['qty'])*price
        qty_per_product += bag[product_spec_id]['qty']
        
        total += total_per_product
        product_count += qty_per_product

        cart_items.append({
            'product_id': product_id,
            'qty_per_product': qty_per_product,
            'product_count': product_count,
            'name': name,
            'paper': paper,
            'size': size,
            'total_per_product': total_per_product,
            'price': price,
            'total': total
        })
        total_per_product = 0
        qty_per_product = 0


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
